# Generated by Django 3.2.25 on 2024-06-21 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('user_id', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='leave',
            fields=[
                ('leave_id', models.AutoField(primary_key=True, serialize=False)),
                ('sendby', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('send_id', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('usertype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='parent',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.login')),
            ],
        ),
        migrations.CreateModel(
            name='upload',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.course')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.course')),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.login')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.parent')),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.login')),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('marks', models.IntegerField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='notice',
            fields=[
                ('notice_id', models.AutoField(primary_key=True, serialize=False)),
                ('notice', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('attendance', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.student')),
            ],
        ),
    ]