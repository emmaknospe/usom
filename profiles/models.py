from django.db import models

class Profile(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class_year = models.IntegerField()

    def stub_find(self):
        split_email = self.email.split("@")
        #if self.email[len(self.email)-12, len(self.email)]:
        #    return ""
        #else:
        #    return self.email[0, len(self.email)-13]
        return split_email[0]

    def pic_url(self):
        stub = self.stub_find()
        if stub != "":
            return "https://apps.carleton.edu/stock/ldapimage.php?id="+stub+"&source=campus_directory"

    def initals(self):
        return self.first_name_name[0] + self.last_name[0]

    def num_orgs(self):
        return len(self.organizations.all())