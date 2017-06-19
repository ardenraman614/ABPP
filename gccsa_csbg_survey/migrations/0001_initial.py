# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Document',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('description', models.CharField(blank=True, max_length=255)),
				('doc_url', models.FileField(upload_to='documents/')),
				('uploaded_at', models.DateTimeField(auto_now_add=True)),
			],
		),
		migrations.CreateModel(
			name='HeadOfHouseholdMember',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('email', models.EmailField(max_length=254, verbose_name='Email')),
				('preferred_phone', models.CharField(choices=[('home', 'Home'), ('mobile', 'Mobile')], max_length=20, verbose_name='Preferred Phone')),
				('preferred_email', models.EmailField(max_length=254, verbose_name='Preferrred contact email address')),
				('preferred_contact_tod', models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon')], max_length=20, verbose_name='Preferrred Time of Contact')),
			],
		),
		migrations.CreateModel(
			name='Household',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('address_1', models.CharField(max_length=128, verbose_name='Address')),
				('city', models.CharField(max_length=64, verbose_name='City')),
				('county', models.CharField(max_length=100, verbose_name='County')),
				('state', localflavor.us.models.USStateField(max_length=2, verbose_name='State')),
				('zip_code', localflavor.us.models.USZipCodeField(max_length=10, verbose_name='Zip Code')),
				('home_phone', localflavor.us.models.PhoneNumberField(blank=True, max_length=20, verbose_name='Home Phone')),
				('type_of_household', models.CharField(choices=[('single_female', 'Single parent female'), ('single_male', 'Single parent male'), ('single_person', 'Single person'), ('two_parent', 'Two parent household'), ('two_adults', 'Two adults'), ('no_children', 'No children'), ('other', 'Other')], max_length=20, verbose_name='Type of Household')),
				('housing_type', models.CharField(choices=[('housing_assistance', 'Housing assistance'), ('apartment', 'Rent an apartment'), ('home_rent', 'Rent a home'), ('homeowner', 'Homeowner'), ('homeless', 'Homeless'), ('live_wtih_relatives', 'Live with relatives'), ('other', 'Other')], max_length=20, verbose_name='Housing Type')),
				('assistance_snap', models.BooleanField(verbose_name='Household receives SNAP')),
				('assistance_caa', models.BooleanField(verbose_name='Household receives assistance from other community agencies')),
				('assistance_child_support', models.BooleanField(verbose_name='Household receives assistance for child support')),
			],
		),
		migrations.CreateModel(
			name='HouseholdMember',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('first_name', models.CharField(error_messages={'required': 'Please let us know what to call you!'}, max_length=100, verbose_name='First Name')),
				('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
				('ssn', localflavor.us.models.USSocialSecurityNumberField(max_length=11, verbose_name='Social Security Number')),
				('mobile_phone', localflavor.us.models.PhoneNumberField(blank=True, max_length=20, verbose_name='Mobile Phone')),
				('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccsa_csbg_survey.Household')),
			],
		),
		migrations.CreateModel(
			name='HouseholdMemberDemographics',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('birthdate', models.DateField(verbose_name='Birth Date')),
				('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20, verbose_name='Gender')),
				('education', models.CharField(choices=[('pre_hs', '0-8 grade'), ('in_hs', '9-12 no high school graduation'), ('hs_grad', 'High school graduate/GED'), ('post_hs', '12+ post sec'), ('college_degree', '2 or 4 year degree')], max_length=20, verbose_name='Education')),
				('race', models.CharField(choices=[('black', 'Black/African American'), ('white', 'White'), ('native', 'American Indian or Alaska Native'), ('asian', 'Asian'), ('multi', 'Multi-race'), ('other', 'Other')], max_length=20, verbose_name='Race')),
				('ethnicity', models.CharField(choices=[('hispanic', 'Hispanic'), ('not_hispanic', 'Not Hispanic')], max_length=20, verbose_name='Ethnicity')),
				('no_health_insurance', models.BooleanField(verbose_name='No Health Insurance')),
				('disabled', models.BooleanField(help_text='Disabled', verbose_name='Disabled')),
				('veteran', models.BooleanField(help_text='Veteran', verbose_name='Veteran')),
				('household_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccsa_csbg_survey.HouseholdMember')),
			],
		),
		migrations.CreateModel(
			name='HouseholdMemberIncome',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('employment', models.CharField(choices=[('employed', 'Employed'), ('not_employed', 'Not employed'), ('self_employed', 'Self employed')], max_length=20, verbose_name='Employment')),
				('pay_period', models.CharField(choices=[('weekly', 'Weekly'), ('biweekly', 'Every two weeks'), ('semi_monthly', 'Twice a month'), ('monthly', 'Monthly'), ('other', 'Other')], max_length=50, verbose_name='Pay Period')),
				('other_income_cash', models.BooleanField(verbose_name='Cash')),
				('other_income_snap', models.BooleanField(verbose_name='SNAP Food Stamps')),
				('other_income_tanf', models.BooleanField(verbose_name='TANF')),
				('other_income_ss', models.BooleanField(verbose_name='Social Security')),
				('other_income_ssdi', models.BooleanField(verbose_name='SSDI/SSI/RSDI')),
				('other_income_medicare', models.BooleanField(verbose_name='Medicare')),
				('other_income_other_agencies', models.BooleanField(verbose_name='Assistance from Other Agencies')),
				('other_income_gifts', models.BooleanField(verbose_name='Gifts')),
				('other_income_unemployment', models.BooleanField(verbose_name='Unemployment')),
				('other_income_workers_comp', models.BooleanField(verbose_name="Worker's Comp")),
				('other_income_pensions', models.BooleanField(verbose_name='Pensions')),
				('other_income_job_training', models.BooleanField(verbose_name='Job Training Stipends')),
				('other_income_military_allotments', models.BooleanField(verbose_name='Military Allotments')),
				('other_income_va', models.BooleanField(verbose_name='VA Benefits')),
				('other_income_insurance', models.BooleanField(verbose_name='Insurance Payment')),
				('other_income_alimony', models.BooleanField(verbose_name='Alimony')),
				('other_income_foster_payments', models.BooleanField(verbose_name='Foster/Adopted Children Payments')),
				('other_income_child_support', models.BooleanField(verbose_name='Court-ordered Child Support')),
				('other_income_college_scholarship', models.BooleanField(verbose_name='College Scholarships')),
				('other_income_student_loans', models.BooleanField(verbose_name='Student Loans')),
				('other_income_other', models.CharField(max_length=50, verbose_name='Other')),
				('household_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccsa_csbg_survey.HouseholdMember')),
			],
		),
		migrations.CreateModel(
			name='HouseholdReferral',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('hear_united_way', models.BooleanField(verbose_name='2-1-1 United Way Hotline')),
				('hear_govt_agency', models.BooleanField(verbose_name='Government Agency')),
				('hear_ss_agency', models.BooleanField(verbose_name='Other Community Agency')),
				('hear_gccsa_client', models.BooleanField(verbose_name='A Former GCCSA Client')),
				('hear_apt_mgr', models.BooleanField(verbose_name='Apartment Manager Referred')),
				('hear_flyer', models.BooleanField(verbose_name='Flyer')),
				('hear_internet', models.BooleanField(verbose_name='GCCSA Website/Internet')),
				('hear_radio_tv', models.BooleanField(verbose_name='Radio, Newspaaper, TV')),
				('hear_other', models.CharField(max_length=50, verbose_name='Other')),
				('headstart_client', models.BooleanField(verbose_name='Are you a head start client')),
				('previous_client', models.CharField(choices=[('first_time_applicant', 'No, I am a first time applicant'), ('0-2_years', 'Yes, 0-2 years ago'), ('3-5_years', 'Yes, 3-5 years ago'), ('over_5_years', 'Yes, over 5 years ago')], max_length=50, verbose_name='Are you, or a Household Member a previous client of GCCSA')),
				('reason_recent_divorce', models.BooleanField(verbose_name='Recent Divorce / Separation')),
				('reason_relocated', models.BooleanField(verbose_name='Relocated to the Area')),
				('reason_unexpected_expenses', models.BooleanField(verbose_name='Unexpected Expenses')),
				('reason_housing_award', models.BooleanField(verbose_name='Change in Housing Award Amount')),
				('reason_job_loss', models.BooleanField(verbose_name='Job Loss')),
				('reason_last_employment_date', models.DateField(blank=True, null=True, verbose_name='Last date of employment')),
				('reason_medical', models.BooleanField(verbose_name='Medical Emergency')),
				('reason_other', models.BooleanField(verbose_name='Other')),
				('reason_details', models.CharField(max_length=4000, verbose_name='Provide details of your household situation')),
				('other_services_rental_assistance', models.BooleanField(verbose_name='Rental Assistance')),
				('other_services_electricity_assistance', models.BooleanField(verbose_name='Electricity Assistance')),
				('other_services_job_readiness', models.BooleanField(verbose_name='Job Readiness Training')),
				('other_services_financial_literacy', models.BooleanField(verbose_name='Financial Literacy')),
				('other_services_housing_counseling', models.BooleanField(verbose_name='Housing Counseling')),
				('other_services_school_supplies', models.BooleanField(verbose_name='School Supplies/Holiday Initiative')),
				('other_services_head_start', models.BooleanField(verbose_name='Head Start/Early Head Start Program')),
				('other_services_vocational_training', models.BooleanField(verbose_name='Scholarship/Vocational Training')),
				('other_services_adult_basic_education', models.BooleanField(verbose_name='GED/Adult Basic Education')),
				('other_services_bus_passes', models.BooleanField(verbose_name='Bus Passes')),
				('other_services_food', models.BooleanField(verbose_name='Emergency Food')),
				('other_services_nutrition', models.BooleanField(verbose_name='Nutrition Services')),
				('other_services_seasonal', models.BooleanField(verbose_name='Seasonal Holiday Initiatives')),
				('case_management', models.BooleanField(verbose_name='Case Management Program')),
				('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccsa_csbg_survey.Household')),
			],
		),
		migrations.CreateModel(
			name='Org',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('org_symbol', models.CharField(db_index=True, max_length=8)),
				('org_product', models.CharField(db_index=True, max_length=8)),
			],
		),
		migrations.CreateModel(
			name='Survey',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('created', models.DateTimeField(auto_now_add=True)),
				('submitted', models.DateTimeField()),
				('survey_id', models.SmallIntegerField()),
				('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccsa_csbg_survey.Org')),
			],
		),
		migrations.AlterUniqueTogether(
			name='org',
			unique_together=set([('org_symbol', 'org_product')]),
		),
		migrations.AddField(
			model_name='household',
			name='survey',
			field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccsa_csbg_survey.Survey'),
		),
		migrations.AddField(
			model_name='headofhouseholdmember',
			name='household_member',
			field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccsa_csbg_survey.HouseholdMember'),
		),
	]