from django.core.urlresolvers import reverse
from django_webtest import WebTest
from model_mommy import mommy
from .models import Task


class TaskTest(WebTest):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Task)
        self.assertTrue(isinstance(instance, Task))

    def test_list_view(self):
        """
        Test that the list view returns at least our factory created instance.
        """
        instance = mommy.make(Task)
        response = self.app.get(reverse('tasks:list'))
        object_list = response.context['object_list']
        self.assertIn(instance, object_list)

    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('tasks:create'))
        new_title = 'A freshly created thing'

        # check that we don't already have a model with this title
        self.assertFalse(Task.objects.filter(title=new_title).exists())

        form = response.forms['task_form']
        form['title'] = new_title
        form.submit().follow()

        instance = Task.objects.get(title=new_title)
        self.assertEqual(instance.title, new_title)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Task)
        response = self.app.get(instance.get_absolute_url())
        self.assertEqual(response.context['object'], instance)

    def test_update_view(self):
        """
        Test that we can update an instance via the update view.
        """
        instance = mommy.make(Task)
        response = self.app.get(reverse('tasks:update', kwargs={'pk': instance.pk, }))

        form = response.forms['task_form']
        new_title = 'Some new thing'
        form['title'] = new_title
        form.submit().follow()

        instance = Task.objects.get(pk=instance.pk)
        self.assertEqual(instance.title, new_title)

    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Task)
        pk = instance.pk
        response = self.app.get(reverse('tasks:delete', kwargs={'pk': pk, }))
        response = response.form.submit().follow()
        self.assertFalse(Task.objects.filter(pk=pk).exists())
