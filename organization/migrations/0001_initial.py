# Generated by Django 2.2 on 2021-03-25 15:12

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='新增时间')),
                ('create_user', models.IntegerField(blank=True, verbose_name='创建者')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='最新修改时间')),
                ('update_user', models.IntegerField(blank=True, verbose_name='修改者')),
                ('name', models.CharField(max_length=200, verbose_name='接口名称')),
                ('path', models.CharField(db_index=True, max_length=200, verbose_name='接口地址')),
                ('format_path', models.CharField(blank=True, db_index=True, default='', max_length=200, verbose_name='格式化接口地址')),
                ('method', models.CharField(max_length=200, verbose_name='方法')),
                ('is_common', models.IntegerField(blank=True, default=0, verbose_name='是否通用接口')),
                ('remark', models.CharField(blank=True, default='', max_length=300, verbose_name='备注')),
            ],
            options={
                'verbose_name': 'api接口表',
                'verbose_name_plural': 'api接口表',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('nick_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='别名')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='全称')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='organization.Department', verbose_name='父级对象')),
            ],
            options={
                'verbose_name': '部门表',
                'verbose_name_plural': '部门表',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='新增时间')),
                ('create_user', models.IntegerField(blank=True, verbose_name='创建者')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='最新修改时间')),
                ('update_user', models.IntegerField(blank=True, verbose_name='修改者')),
                ('name', models.CharField(max_length=200, verbose_name='节点名称')),
                ('icon', models.CharField(blank=True, default='', max_length=100, verbose_name='节点图标')),
                ('is_show', models.IntegerField(blank=True, default=1, verbose_name='是否显示')),
                ('order_num', models.IntegerField(blank=True, db_index=True, default=0, help_text='0-99数值越小，顺序越靠前', verbose_name='排序号')),
                ('type', models.IntegerField(choices=[(0, '目录'), (1, '菜单'), (2, '权限')], verbose_name='类型')),
                ('is_keep_alive', models.IntegerField(blank=True, default=1, verbose_name='页面是否缓存')),
                ('path', models.CharField(blank=True, default='', max_length=200, verbose_name='路由地址')),
                ('view_path', models.CharField(blank=True, default='', max_length=200, verbose_name='文件路径')),
                ('api', models.ManyToManyField(related_name='menu', to='organization.Api')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.Menu', verbose_name='父级对象')),
            ],
            options={
                'verbose_name': '权限表',
                'verbose_name_plural': '权限表',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='新增时间')),
                ('create_user', models.IntegerField(blank=True, verbose_name='创建者')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='最新修改时间')),
                ('update_user', models.IntegerField(blank=True, verbose_name='修改者')),
                ('name', models.CharField(db_index=True, help_text='角色名称唯一，admin为超级管理员', max_length=200, unique=True, verbose_name='名称')),
                ('label', models.CharField(max_length=200, verbose_name='标识')),
                ('remark', models.CharField(blank=True, default='', max_length=200, verbose_name='备注')),
                ('department', models.ManyToManyField(related_name='department', to='organization.Department')),
                ('menu', models.ManyToManyField(related_name='role', to='organization.Menu')),
            ],
            options={
                'verbose_name': '角色表',
                'verbose_name_plural': '角色表',
                'ordering': ['create_datetime'],
            },
        ),
        migrations.CreateModel(
            name='UserBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='新增时间')),
                ('create_user', models.IntegerField(blank=True, verbose_name='创建者')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='最新修改时间')),
                ('update_user', models.IntegerField(blank=True, verbose_name='修改者')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('name', models.CharField(max_length=50, verbose_name='昵称')),
                ('sex', models.IntegerField(blank=True, choices=[(0, '女'), (1, '男'), (2, '未知')], default=1)),
                ('mobile', models.CharField(blank=True, default='', max_length=11, verbose_name='手机')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('head_image', models.FileField(blank=True, default='', max_length=1024, null=True, upload_to='image/%Y/%m', verbose_name='头像')),
                ('is_active', models.IntegerField(blank=True, choices=[(0, '停用'), (1, '正常')], default=1, verbose_name='状态')),
                ('remark', models.CharField(blank=True, default='', max_length=200, verbose_name='备注')),
                ('department', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='organization.Department', verbose_name='部门')),
                ('role', models.ManyToManyField(related_name='user_base', to='organization.Role')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'ordering': ['create_datetime'],
                'get_latest_by': 'create_datetime',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddIndex(
            model_name='userbase',
            index=models.Index(fields=['name'], name='organizatio_name_759324_idx'),
        ),
        migrations.AddIndex(
            model_name='userbase',
            index=models.Index(fields=['mobile'], name='organizatio_mobile_ca69ab_idx'),
        ),
        migrations.AddIndex(
            model_name='userbase',
            index=models.Index(fields=['department'], name='organizatio_departm_29282d_idx'),
        ),
    ]
