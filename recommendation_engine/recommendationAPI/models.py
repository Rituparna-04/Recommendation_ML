# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Tblcourseinfo(models.Model):
    courseinfoid = models.IntegerField(db_column='CourseInfoId', primary_key=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId', unique=True)  # Field name made lowercase.
    coursename = models.TextField(db_column='CourseName', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId')  # Field name made lowercase.
    subjectname = models.TextField(db_column='SubjectName')  # Field name made lowercase.
    skillid = models.IntegerField(db_column='SkillId')  # Field name made lowercase.
    skillname = models.TextField(db_column='SkillName')  # Field name made lowercase.
    providerid = models.IntegerField(db_column='ProviderId')  # Field name made lowercase.
    providername = models.TextField(db_column='ProviderName')  # Field name made lowercase.
    coursepatternid = models.IntegerField(db_column='CoursePatternId')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CreatedBy')  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='UpdatedBy')  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblCourseInfo'


class Tblcourseratings(models.Model):
    courseratingid = models.IntegerField(db_column='CourseRatingId', primary_key=True)  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseId')  # Field name made lowercase.
    rating = models.DecimalField(db_column='Rating', max_digits=4, decimal_places=2)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CreatedBy')  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='UpdatedBy')  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tblCourseRatings'
        unique_together = (('createdby', 'courseid'),)

