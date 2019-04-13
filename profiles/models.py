from django.db import models

class Profile(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class_year = models.IntegerField()
    # TODO: picture from stalkernet

    def stub_find(self):
        if self.email[len(self.email)-12, len(self.email)]:
            return ""
        else:
            return self.email[0, len(self.email)-13]

    def pic_url(self):
        stub = self.stub_find(self)
        if stub != "":
            return "https://apps.carleton.edu/stock/ldapimage.php?id="+stub+"&source=campus_directory"
