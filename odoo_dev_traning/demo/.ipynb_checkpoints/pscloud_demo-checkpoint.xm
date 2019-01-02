<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>

        <record id="demo_training_person" model="res.partner">
            <field eval="'徐校长'" name="name"/>
        </record>

        <record id="demo_training_teacher" model="res.partner">
            <field eval="'王老师'" name="name"/>
            <field eval="True" name="is_teacher"/>
        </record>

        <record id="demo_training_student_1" model="res.partner">
            <field eval="'学生1'" name="name"/>
            <field eval="True" name="is_student"/>
        </record>

        <record id="demo_training_student_2" model="res.partner">
            <field eval="'学生2'" name="name"/>
            <field eval="True" name="is_student"/>
        </record>

        <record id="demo_training_subject" model="pscloud.training.subject">
            <field eval="'大学英语'" name="name"/>
            <field name="person_id" ref="pscloud_training.demo_training_person"/>
            <field eval="'好好学习，天天向上'" name="desc"/>
        </record>

        <record id="demo_training_lesson_1" model="pscloud.training.lesson">
            <field eval="'英语口语'" name="name"/>
            <field name="teacher_id" ref="pscloud_training.demo_training_teacher"/>
            <field eval="[(4, ref('pscloud_training.demo_training_student_1'))]" name="student_ids"/>
            <field eval="time.strftime('%Y')+'-09-01'" name="start_date"/>
            <field eval="time.strftime('%Y')+'-12-31'" name="end_date"/>
            <field eval="30" name="seat_qty"/>
            <field name="subject_id" ref="pscloud_training.demo_training_subject"/>
        </record>

    </data>
</odoo>