from django.db import models

# Create a data object to store information about the places

class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    visited_date = models.DateTimeField(blank=True, null=True)
    note = models.TextField(default='')

    #updates the date visited to the current time, later it will accept user input to set the date it was visited
    def visit(self):
        self.visited_date = timezone.now()
        self.save()


    def __str__(self):
        return '%s visited? %s' % (self.name, self.visited)
