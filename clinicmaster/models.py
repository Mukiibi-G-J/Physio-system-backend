from django.db import models


# class Parishes(models.Model):
#     parishcode = models.CharField(db_column='ParishCode', primary_key=True, max_length=20)  # Field name made lowercase.
#     parishname = models.CharField(db_column='ParishName', max_length=41, blank=True, null=True)  # Field name made lowercase.
#     subcountycode = models.ForeignKey('Subcounties', models.DO_NOTHING, db_column='SubCountyCode', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Parishes'
#         unique_together = (('parishname', 'subcountycode'),)

# class Villages(models.Model):
#     villagecode = models.CharField(db_column='VillageCode', primary_key=True, max_length=20)  # Field name made lowercase.
#     villagename = models.CharField(db_column='VillageName', max_length=41, blank=True, null=True)  # Field name made lowercase.
#     parishcode = models.ForeignKey(Parishes, models.DO_NOTHING, db_column='ParishCode', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Villages'
#         unique_together = (('villagename', 'parishcode'),)


# class Healthunits(models.Model):
#     healthunitcode = models.CharField(db_column='HealthUnitCode', primary_key=True, max_length=10)  # Field name made lowercase.
#     healthunitname = models.CharField(db_column='HealthUnitName', unique=True, max_length=41, blank=True, null=True)  # Field name made lowercase.
#     districtsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DistrictsID', blank=True, null=True)  # Field name made lowercase.
#     contactperson = models.CharField(db_column='ContactPerson', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
# db_table = 'HealthUnits'

# class Logins(models.Model):
#     loginid = models.CharField(db_column='LoginID', primary_key=True, max_length=20)  # Field name made lowercase.
#     firstname = models.CharField(db_column='FirstName', max_length=20)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', max_length=20)  # Field name made lowercase.
#     loginpassword = models.CharField(db_column='LoginPassword', max_length=200)  # Field name made lowercase.
#     loginlevel = models.SmallIntegerField(db_column='LoginLevel')  # Field name made lowercase.
#     statusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='StatusID')  # Field name made lowercase.
#     changepassword = models.BooleanField(db_column='ChangePassword')  # Field name made lowercase.
#     creatorloginid = models.ForeignKey('self', models.DO_NOTHING, db_column='CreatorLoginID', blank=True, null=True)  # Field name made lowercase.
#     creatorclientmachine = models.CharField(db_column='CreatorClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     creatorrecorddatetime = models.DateTimeField(db_column='CreatorRecordDateTime', blank=True, null=True)  # Field name made lowercase.

#     class Meta:


#         db_table = 'Logins'
class Lookupdata(models.Model):
    # lookuporder = models.AutoField(db_column='LookupOrder')  # Field name made lowercase.
    dataid = models.CharField(
        db_column="DataID", primary_key=True, max_length=10
    )  # Field name made lowercase.
    #     objectid = models.ForeignKey('Lookupobjects', models.DO_NOTHING, db_column='ObjectID')  # Field name made lowercase.
    datades = models.CharField(
        db_column="DataDes", max_length=100
    )  # Field name made lowercase.
    #     isdefault = models.CharField(db_column='IsDefault', max_length=1)  # Field name made lowercase.
    #     ishidden = models.CharField(db_column='IsHidden', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = "LookupData"
        # unique_together = (('objectid', 'datades'),)


class Patients(models.Model):
    patientid = models.IntegerField(db_column="PatientID")  # Field name made lowercase.
    patientno = models.CharField(
        db_column="PatientNo", primary_key=True, max_length=20
    )  # Field name made lowercase.
    referenceno = models.CharField(
        db_column="ReferenceNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    firstname = models.CharField(
        db_column="FirstName", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    lastname = models.CharField(
        db_column="LastName", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    middlename = models.CharField(
        db_column="MiddleName", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    birthdate = models.DateTimeField(
        db_column="BirthDate", blank=True, null=True
    )  # Field name made lowercase.
    genderid = models.ForeignKey(
        Lookupdata, models.DO_NOTHING, db_column="GenderID", blank=True, null=True
    )  # Field name made lowercase.
    photo = models.BinaryField(
        db_column="Photo", blank=True, null=True
    )  # Field name made lowercase.
    fingerprint = models.BinaryField(
        db_column="Fingerprint", blank=True, null=True
    )  # Field name made lowercase.
    birthplace = models.CharField(
        db_column="BirthPlace", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    address = models.CharField(
        db_column="Address", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    occupation = models.CharField(
        db_column="Occupation", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    phone = models.CharField(
        db_column="Phone", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    email = models.CharField(
        db_column="Email", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    joindate = models.DateTimeField(
        db_column="JoinDate", blank=True, null=True
    )  # Field name made lowercase.
    location = models.CharField(
        db_column="Location", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    nokname = models.CharField(
        db_column="NOKName", max_length=41, blank=True, null=True
    )  # Field name made lowercase.
    nokrelationship = models.CharField(
        db_column="NOKRelationship", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    nokphone = models.CharField(
        db_column="NOKPhone", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    defaultbillmodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DefaultBillModesID', blank=True, null=True, related_name="default_billMode")  # Field name made lowercase.
    defaultbillno = models.CharField(
        db_column="DefaultBillNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    defaultmembercardno = models.CharField(
        db_column="DefaultMemberCardNo", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    defaultmainmembername = models.CharField(
        db_column="DefaultMainMemberName", max_length=41, blank=True, null=True
    )  # Field name made lowercase.
    enforcedefaultbillno = models.BooleanField(
        db_column="EnforceDefaultBillNo"
    )  # Field name made lowercase.
    hidedetails = models.BooleanField(
        db_column="HideDetails", blank=True, null=True
    )  # Field name made lowercase.
    # statusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='StatusID', blank=True, null=True)  # Field name made lowercase.
    # bloodgroupid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BloodGroupID', blank=True, null=True)  # Field name made lowercase.
    # villagecode = models.ForeignKey('Villages', models.DO_NOTHING, db_column='VillageCode', blank=True, null=True)  # Field name made lowercase.
    # tribeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='TribeID', blank=True, null=True)  # Field name made lowercase.
    # countryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    # maritalstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='MaritalStatusID', blank=True, null=True)  # Field name made lowercase.
    # careentrypointid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CareEntryPointID', blank=True, null=True)  # Field name made lowercase.
    # religionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ReligionID', blank=True, null=True)  # Field name made lowercase.
    # employer = models.CharField(db_column='Employer', max_length=41, blank=True, null=True)  # Field name made lowercase.
    employeraddress = models.CharField(
        db_column="EmployerAddress", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    referringmedicalofficer = models.CharField(
        db_column="ReferringMedicalOfficer", max_length=41, blank=True, null=True
    )  # Field name made lowercase.
    nearestdispensary = models.CharField(
        db_column="NearestDispensary", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    previousadmissions = models.CharField(
        db_column="PreviousAdmissions", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    chronicdiseases = models.CharField(
        db_column="ChronicDiseases", max_length=200, blank=True, null=True
    )  # Field name made lowercase.
    firstvisitdate = models.DateTimeField(
        db_column="FirstVisitDate", blank=True, null=True
    )  # Field name made lowercase.
    lastvisitdate = models.DateTimeField(
        db_column="LastVisitDate", blank=True, null=True
    )  # Field name made lowercase.
    combinationon = models.CharField(
        db_column="CombinationOn", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    totalvisits = models.IntegerField(
        db_column="TotalVisits", blank=True, null=True
    )  # Field name made lowercase.
    accountbalance = models.DecimalField(
        db_column="AccountBalance",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    # loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(
        db_column="ClientMachine", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    recorddatetime = models.DateTimeField(
        db_column="RecordDateTime", blank=True, null=True
    )  # Field name made lowercase.
    nationalidno = models.CharField(
        db_column="NationalIDNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    # branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    xraynumbers = models.DecimalField(
        db_column="XrayNumbers", max_digits=6, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    policenotified = models.BooleanField(
        db_column="PoliceNotified"
    )  # Field name made lowercase.
    infectiousdiseasesnotified = models.BooleanField(
        db_column="InfectiousDiseasesNotified"
    )  # Field name made lowercase.
    medicalconditions = models.CharField(
        db_column="MedicalConditions", max_length=2000, blank=True, null=True
    )  # Field name made lowercase.
    provisionaldiagnosis = models.CharField(
        db_column="ProvisionalDiagnosis", max_length=2000, blank=True, null=True
    )  # Field name made lowercase.
    # communityid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CommunityID', blank=True, null=True)  # Field name made lowercase.
    # educationlevelid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='EducationLevelID', blank=True, null=True)  # Field name made lowercase.
    referringfacility = models.CharField(
        db_column="ReferringFacility", max_length=41, blank=True, null=True
    )  # Field name made lowercase.
    # attachedtoid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AttachedToID', blank=True, null=True)  # Field name made lowercase.
    # healthunitcode = models.ForeignKey(Healthunits, models.DO_NOTHING, db_column='HealthUnitCode', blank=True, null=True)  # Field name made lowercase.
    # accountstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AccountStatusID', blank=True, null=True)  # Field name made lowercase.
    opdoutstanding = models.DecimalField(
        db_column="OPDOutstanding",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    extrabilloutstanding = models.DecimalField(
        db_column="ExtraBillOutstanding",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    lastaccountactiondate = models.DateTimeField(
        db_column="LastAccountActionDate", blank=True, null=True
    )  # Field name made lowercase.
    knowaboutservice = models.CharField(
        db_column="KnowAboutService", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    # clientcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ClientCategoryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = "Patients"


class Items(models.Model):
    visitno = models.OneToOneField(
        "Visits", models.DO_NOTHING, db_column="VisitNo", primary_key=True
    )  # Field name made lowercase.
    itemcode = models.CharField(
        db_column="ItemCode", max_length=20
    )  # Field name made lowercase.
    # itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    quantity = models.IntegerField(
        db_column="Quantity", blank=True, null=True
    )  # Field name made lowercase.
    unitcost = models.DecimalField(
        db_column="UnitCost", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    unitprice = models.DecimalField(
        db_column="UnitPrice", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    itemdetails = models.CharField(
        db_column="ItemDetails", max_length=800, blank=True, null=True
    )  # Field name made lowercase.
    lastupdate = models.DateTimeField(
        db_column="LastUpdate", blank=True, null=True
    )  # Field name made lowercase.
    # itemstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemStatusID', blank=True, null=True)  # Field name made lowercase.
    # paystatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayStatusID', blank=True, null=True)  # Field name made lowercase.
    # loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(
        db_column="ClientMachine", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    recorddatetime = models.DateTimeField(
        db_column="RecordDateTime", blank=True, null=True
    )  # Field name made lowercase.
    creatorclientmachine = models.CharField(
        db_column="CreatorClientMachine", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    # creatorloginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='CreatorLoginID', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(
        db_column="ItemName", max_length=800, blank=True, null=True
    )  # Field name made lowercase.
    unitmeasure = models.CharField(
        db_column="UnitMeasure", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    vatvalue = models.DecimalField(
        db_column="VATValue", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    invoiceno = models.CharField(
        db_column="InvoiceNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    originalquantity = models.IntegerField(
        db_column="OriginalQuantity", blank=True, null=True
    )  # Field name made lowercase.
    originalprice = models.DecimalField(
        db_column="OriginalPrice",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    conclusiondate = models.DateTimeField(
        db_column="ConclusionDate", blank=True, null=True
    )  # Field name made lowercase.
    paydate = models.DateTimeField(
        db_column="PayDate", blank=True, null=True
    )  # Field name made lowercase.
    adjustmentcount = models.IntegerField(
        db_column="AdjustmentCount", blank=True, null=True
    )  # Field name made lowercase.
    discount = models.DecimalField(
        db_column="Discount", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    # referenceno = models.ForeignKey('Paymentrequests', models.DO_NOTHING, db_column='ReferenceNo', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.itemcode

    class Meta:
        db_table = "Items"
        # unique_together = (('visitno', 'itemcode', 'itemcategoryid'), ('visitno', 'itemcategoryid', 'itemcode'),)
        unique_together = (
            ("visitno", "itemcode"),
            ("visitno", "itemcode"),
        )

    def __str__(self):
        return self.itemcode


class Visits(models.Model):
    visitid = models.IntegerField(db_column="VisitID")  # Field name made lowercase.
    visitno = models.CharField(
        db_column="VisitNo", primary_key=True, max_length=20
    )  # Field name made lowercase.
    patientno = models.ForeignKey(
        Patients,
        models.DO_NOTHING,
        db_column="PatientNo",
        blank=True,
        null=True,
        related_name="patient_table",
    )  # Field name made lowercase.
    visitdate = models.DateTimeField(
        db_column="VisitDate", blank=True, null=True
    )  # Field name made lowercase.
    # doctorspecialtyid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DoctorSpecialtyID', blank=True, null=True)  # Field name made lowercase.
    # staffno = models.ForeignKey(Staff, models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    # visitcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisitCategoryID', blank=True, null=True)  # Field name made lowercase.
    referredby = models.CharField(
        db_column="ReferredBy", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    # servicecode = models.ForeignKey(Services, models.DO_NOTHING, db_column='ServiceCode', blank=True, null=True)  # Field name made lowercase.
    billmodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BillModesID', blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(
        db_column="BillNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    insuranceno = models.CharField(
        db_column="InsuranceNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    # associatedbillno = models.ForeignKey(Billcustomers, models.DO_NOTHING, db_column='AssociatedBillNo', blank=True, null=True)  # Field name made lowercase.
    membercardno = models.CharField(
        db_column="MemberCardNo", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    mainmembername = models.CharField(
        db_column="MainMemberName", max_length=41, blank=True, null=True
    )  # Field name made lowercase.
    claimreferenceno = models.CharField(
        db_column="ClaimReferenceNo", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    # visitstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisitStatusID', blank=True, null=True)  # Field name made lowercase.
    accesscashservices = models.BooleanField(
        db_column="AccessCashServices", blank=True, null=True
    )  # Field name made lowercase.
    fingerprintverified = models.BooleanField(
        db_column="FingerprintVerified", blank=True, null=True
    )  # Field name made lowercase.
    # copaytypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CoPayTypeID', blank=True, null=True)  # Field name made lowercase.
    copaypercent = models.DecimalField(
        db_column="CoPayPercent", max_digits=5, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    copayvalue = models.DecimalField(
        db_column="CoPayValue", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    smartcardapplicable = models.BooleanField(
        db_column="SmartCardApplicable", blank=True, null=True
    )  # Field name made lowercase.
    # loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(
        db_column="ClientMachine", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    recorddatetime = models.DateTimeField(
        db_column="RecordDateTime", blank=True, null=True
    )  # Field name made lowercase.
    # visitspriorityid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisitsPriorityID', blank=True, null=True)  # Field name made lowercase.
    locked = models.BooleanField(
        db_column="Locked", blank=True, null=True
    )  # Field name made lowercase.
    # branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    # communityid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CommunityID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = "Visits"

    def __str__(self):
        return self.visitno


class Paymentdetails(models.Model):
    receiptno = models.OneToOneField(
        "Payments", models.DO_NOTHING, db_column="ReceiptNo", primary_key=True
    )  # Field name made lowercase.
    visitno = models.ForeignKey(
        Items, models.DO_NOTHING, db_column="VisitNo", related_name="items_vistno"
    )  # Field name made lowercase.
    itemcode = models.ForeignKey(
        Items, models.DO_NOTHING, db_column="ItemCode", related_name="items_itemcode"
    )  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(
        Items, models.DO_NOTHING, db_column="ItemCategoryID"
    )  # Field name made lowercase.
    quantity = models.IntegerField(
        db_column="Quantity", blank=True, null=True
    )  # Field name made lowercase.
    unitprice = models.DecimalField(
        db_column="UnitPrice", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    discount = models.DecimalField(
        db_column="Discount", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    amount = models.DecimalField(
        db_column="Amount", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    syncstatus = models.BooleanField(
        db_column="SyncStatus", blank=True, null=True
    )  # Field name made lowercase.
    invoiceno = models.CharField(
        db_column="InvoiceNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    # visittypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisitTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = "PaymentDetails"
        unique_together = (
            ("receiptno", "visitno", "itemcode", "itemcategoryid", "itemcategoryid"),
        )

    def __str__(self):
        return self.receiptno.receiptno

    def my_itemcode(self):
        return self.itemcode


class Payments(models.Model):
    receiptid = models.IntegerField(db_column="ReceiptID")  # Field name made lowercase.
    receiptno = models.CharField(
        db_column="ReceiptNo", primary_key=True, max_length=20
    )  # Field name made lowercase.
    # paytypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PayTypeID', blank=True, null=True)  # Field name made lowercase.
    payno = models.CharField(
        db_column="PayNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    paydate = models.DateTimeField(
        db_column="PayDate", blank=True, null=True
    )  # Field name made lowercase.
    # paymodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PayModesID', blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(
        db_column="DocumentNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    amountwords = models.CharField(
        db_column="AmountWords", max_length=200, blank=True, null=True
    )  # Field name made lowercase.
    notes = models.CharField(
        db_column="Notes", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    # currenciesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CurrenciesID', blank=True, null=True)  # Field name made lowercase.
    amounttendered = models.DecimalField(
        db_column="AmountTendered",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exchangerate = models.DecimalField(
        db_column="ExchangeRate", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    change = models.DecimalField(
        db_column="Change", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    sendbalancetoaccount = models.BooleanField(
        db_column="SendBalanceToAccount", blank=True, null=True
    )  # Field name made lowercase.
    useaccountbalance = models.BooleanField(
        db_column="UseAccountBalance", blank=True, null=True
    )  # Field name made lowercase.
    # filterno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='FilterNo', blank=True, null=True)  # Field name made lowercase.
    # loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(
        db_column="ClientMachine", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    recorddatetime = models.DateTimeField(
        db_column="RecordDateTime", blank=True, null=True
    )  # Field name made lowercase.
    # branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    clientfullname = models.CharField(
        db_column="ClientFullName", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    withholdingtax = models.DecimalField(
        db_column="WithholdingTax",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    granddiscount = models.DecimalField(
        db_column="GrandDiscount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    amount = models.DecimalField(
        db_column="Amount", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    cashamount = models.DecimalField(
        db_column="CashAmount", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Payments"


class Extrabills(models.Model):
    extrabillid = models.IntegerField(
        db_column="ExtraBillID"
    )  # Field name made lowercase.
    extrabillno = models.CharField(
        db_column="ExtraBillNo", primary_key=True, max_length=20
    )  # Field name made lowercase.
    visitno = models.ForeignKey(
        "Visits", models.DO_NOTHING, db_column="VisitNo", blank=True, null=True
    )  # Field name made lowercase.
    extrabilldate = models.DateTimeField(
        db_column="ExtraBillDate", blank=True, null=True
    )  # Field name made lowercase.
    # staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    # loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(
        db_column="RecordDateTime", blank=True, null=True
    )  # Field name made lowercase.
    # visittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisitTypeID', blank=True, null=True)  # Field name made lowercase.
    billmodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BillModesID', blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(
        db_column="BillNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    insuranceno = models.CharField(
        db_column="InsuranceNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    # associatedbillno = models.ForeignKey(Billcustomers, models.DO_NOTHING, db_column='AssociatedBillNo', blank=True, null=True)  # Field name made lowercase.
    membercardno = models.CharField(
        db_column="MemberCardNo", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    mainmembername = models.CharField(
        db_column="MainMemberName", max_length=41, blank=True, null=True
    )  # Field name made lowercase.
    claimreferenceno = models.CharField(
        db_column="ClaimReferenceNo", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    # copaytypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CoPayTypeID', blank=True, null=True)  # Field name made lowercase.
    copaypercent = models.DecimalField(
        db_column="CoPayPercent", max_digits=5, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    copayvalue = models.DecimalField(
        db_column="CoPayValue", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    accesscashservices = models.BooleanField(
        db_column="AccessCashServices", blank=True, null=True
    )  # Field name made lowercase.
    smartcardapplicable = models.BooleanField(
        db_column="SmartCardApplicable", blank=True, null=True
    )  # Field name made lowercase.
    amount = models.DecimalField(
        db_column="Amount", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    amountpaid = models.DecimalField(
        db_column="AmountPaid", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    # paytypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayTypeID', blank=True, null=True)  # Field name made lowercase.
    associatedextrabillno = models.ForeignKey(
        "self",
        models.DO_NOTHING,
        db_column="AssociatedExtraBillNo",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    originalamount = models.DecimalField(
        db_column="OriginalAmount",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        db_table = "ExtraBills"


class Admissions(models.Model):
    admissionid = models.IntegerField(
        db_column="AdmissionID"
    )  # Field name made lowercase.
    admissionno = models.CharField(
        db_column="AdmissionNo", primary_key=True, max_length=20
    )  # Field name made lowercase.
    visitno = models.OneToOneField(
        "Visits", models.DO_NOTHING, db_column="VisitNo", blank=True, null=True
    )  # Field name made lowercase.
    # staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    # bedno = models.ForeignKey('Beds', models.DO_NOTHING, db_column='BedNo', blank=True, null=True)  # Field name made lowercase.
    admissiondatetime = models.DateTimeField(
        db_column="AdmissionDateTime", blank=True, null=True
    )  # Field name made lowercase.
    admissionnotes = models.CharField(
        db_column="AdmissionNotes", max_length=2000, blank=True, null=True
    )  # Field name made lowercase.
    admissionstatusid = models.ForeignKey(
        "Lookupdata",
        models.DO_NOTHING,
        db_column="AdmissionStatusID",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    # loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(
        db_column="ClientMachine", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    recorddatetime = models.DateTimeField(
        db_column="RecordDateTime", blank=True, null=True
    )  # Field name made lowercase.
    chartnumber = models.CharField(
        db_column="ChartNumber", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    # billmodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BillModesID', blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(
        db_column="BillNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    insuranceno = models.CharField(
        db_column="InsuranceNo", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    # associatedbillno = models.ForeignKey('Billcustomers', models.DO_NOTHING, db_column='AssociatedBillNo', blank=True, null=True)  # Field name made lowercase.
    membercardno = models.CharField(
        db_column="MemberCardNo", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    mainmembername = models.CharField(
        db_column="MainMemberName", max_length=41, blank=True, null=True
    )  # Field name made lowercase.
    claimreferenceno = models.CharField(
        db_column="ClaimReferenceNo", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    # copaytypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CoPayTypeID', blank=True, null=True)  # Field name made lowercase.
    copaypercent = models.DecimalField(
        db_column="CoPayPercent", max_digits=5, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    copayvalue = models.DecimalField(
        db_column="CoPayValue", max_digits=19, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.
    accesscashservices = models.BooleanField(
        db_column="AccessCashServices", blank=True, null=True
    )  # Field name made lowercase.
    smartcardapplicable = models.BooleanField(
        db_column="SmartCardApplicable", blank=True, null=True
    )  # Field name made lowercase.
    patientno = models.ForeignKey(
        "Patients", models.DO_NOTHING, db_column="PatientNo", blank=True, null=True
    )  # Field name made lowercase.
    # servicecode = models.ForeignKey('Services', models.DO_NOTHING, db_column='ServiceCode', blank=True, null=True)  # Field name made lowercase.
    provisionaldiagnosis = models.CharField(
        db_column="ProvisionalDiagnosis", max_length=2000, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        db_table = "Admissions"



class Discharges(models.Model):
    admissionno = models.OneToOneField(Admissions, models.DO_NOTHING, db_column='AdmissionNo', primary_key=True)  # Field name made lowercase.
    # staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    # roundno = models.ForeignKey('Ipddoctor', models.DO_NOTHING, db_column='RoundNo', blank=True, null=True)  # Field name made lowercase.
    dischargedatetime = models.DateTimeField(db_column='DischargeDateTime', blank=True, null=True)  # Field name made lowercase.
    dischargenotes = models.CharField(db_column='DischargeNotes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    # dischargestatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DischargeStatusID', blank=True, null=True)  # Field name made lowercase.
    reviewdate = models.DateTimeField(db_column='ReviewDate', blank=True, null=True)  # Field name made lowercase.
    history = models.CharField(db_column='History', max_length=400, blank=True, null=True)  # Field name made lowercase.
    examination = models.CharField(db_column='Examination', max_length=400, blank=True, null=True)  # Field name made lowercase.
    keyfindingsinvestigation = models.CharField(db_column='KeyFindingsInvestigation', max_length=400, blank=True, null=True)  # Field name made lowercase.
    treatmentplan = models.CharField(db_column='TreatmentPlan', max_length=400, blank=True, null=True)  # Field name made lowercase.
    outcomeoftreatment = models.CharField(db_column='OutcomeOfTreatment', max_length=400, blank=True, null=True)  # Field name made lowercase.
    keyrecommendations = models.CharField(db_column='KeyRecommendations', max_length=400, blank=True, null=True)  # Field name made lowercase.
    # loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    # dischargewardid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DischargeWardID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Discharges'


class Octbills(models.Model):
    ipd_extra_bill_no = models.CharField(db_column='IPD_Extra_Bill_No', max_length=50)  # Field name made lowercase.
    patient_id = models.CharField(db_column='Patient_ID', max_length=50)  # Field name made lowercase.
    transaction_date_dt = models.CharField(db_column='Transaction_Date_DT', max_length=50)  # Field name made lowercase.
    no = models.CharField(db_column='No', max_length=50)  # Field name made lowercase.
    visit_no = models.CharField(db_column='Visit_No', max_length=50)  # Field name made lowercase.
    item_category_code = models.CharField(db_column='Item_Category_Code', max_length=50)  # Field name made lowercase.
    transaction_date = models.DateTimeField(db_column='Transaction_Date', blank=True, null=True)  # Field name made lowercase.
    package_code = models.CharField(db_column='Package_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    package_id = models.CharField(db_column='Package_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bill_to_customer_no = models.CharField(db_column='Bill_To_Customer_No', max_length=50)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    unit_of_measure = models.CharField(db_column='Unit_of_Measure', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unit_price = models.IntegerField(db_column='Unit_Price')  # Field name made lowercase.
    lot_no = models.CharField(db_column='Lot_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expiry_date = models.DateTimeField(db_column='Expiry_Date')  # Field name made lowercase.

    class Meta:
    
        db_table = 'OctBills'



class Invoices(models.Model):
    invoiceid = models.IntegerField(db_column='InvoiceID')  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', primary_key=True, max_length=20)  # Field name made lowercase.
    # paytypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayTypeID', blank=True, null=True)  # Field name made lowercase.
    payno = models.CharField(db_column='PayNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    amountwords = models.CharField(db_column='AmountWords', max_length=200, blank=True, null=True)  # Field name made lowercase.
    # loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    locked = models.BooleanField(db_column='Locked', blank=True, null=True)  # Field name made lowercase.
    cancelled = models.BooleanField(db_column='Cancelled', blank=True, null=True)  # Field name made lowercase.
    # entrymodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EntryModeID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountpaid = models.DecimalField(db_column='AmountPaid', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Invoices'
        
    
    
class Novbills(models.Model):
    ipd_extra_bill_no = models.CharField(db_column='IPD_Extra_Bill_No', max_length=50)  # Field name made lowercase.
    patient_id = models.CharField(db_column='Patient_ID', max_length=50)  # Field name made lowercase.
    transaction_date_dt = models.CharField(db_column='Transaction_Date_DT', max_length=50)  # Field name made lowercase.
    no = models.CharField(db_column='No', max_length=50)  # Field name made lowercase.
    visit_no = models.CharField(db_column='Visit_No', max_length=50)  # Field name made lowercase.
    item_category_code = models.CharField(db_column='Item_Category_Code', max_length=50)  # Field name made lowercase.
    transaction_date = models.DateTimeField(db_column='Transaction_Date', blank=True, null=True)  # Field name made lowercase.
    package_code = models.CharField(db_column='Package_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    package_id = models.CharField(db_column='Package_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bill_to_customer_no = models.CharField(db_column='Bill_To_Customer_No', max_length=50)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    unit_of_measure = models.CharField(db_column='Unit_of_Measure', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unit_price = models.IntegerField(db_column='Unit_Price')  # Field name made lowercase.
    lot_no = models.CharField(db_column='Lot_No', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expiry_date = models.DateTimeField(db_column='Expiry_Date')  # Field name made lowercase.

    class Meta:
        db_table = 'NovBills'

class Newoctbills(models.Model):
    invoice_no = models.CharField(db_column='Invoice_No', max_length=50)  # Field name made lowercase.
    no = models.CharField(db_column='No', max_length=50)  # Field name made lowercase.
    bill_to_customer_no = models.CharField(db_column='Bill_to_customer_No', max_length=50)  # Field name made lowercase.
    posting_date = models.DateTimeField(db_column='Posting_Date', blank=True, null=True)  # Field name made lowercase.
    item_category_code = models.CharField(db_column='Item_Category_Code', max_length=50)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    location_code = models.CharField(db_column='Location_Code', max_length=1, blank=True, null=True)  # Field name made lowercase.
    quantity_invoiced = models.IntegerField(db_column='Quantity_Invoiced')  # Field name made lowercase.
    unit_of_measure = models.CharField(db_column='Unit_of_Measure', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unit_price = models.IntegerField(db_column='Unit_price')  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount')  # Field name made lowercase.
    lot_no_field = models.CharField(db_column='Lot_No_', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    expiry_date = models.DateTimeField(db_column='Expiry_date')  # Field name made lowercase.
    completed = models.IntegerField(db_column='Completed')  # Field name made lowercase.
    package_code = models.CharField(db_column='Package_Code', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'NewOctBills'


class Newnovbills(models.Model):
    invoice_no = models.CharField(db_column='Invoice_No', max_length=50)  # Field name made lowercase.
    no = models.CharField(db_column='No', max_length=50)  # Field name made lowercase.
    bill_to_customer_no = models.CharField(db_column='Bill_to_customer_No', max_length=50)  # Field name made lowercase.
    posting_date = models.DateTimeField(db_column='Posting_Date', blank=True, null=True)  # Field name made lowercase.
    item_category_code = models.CharField(db_column='Item_Category_Code', max_length=50)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    location_code = models.CharField(db_column='Location_Code', max_length=1, blank=True, null=True)  # Field name made lowercase.
    quantity_invoiced = models.IntegerField(db_column='Quantity_Invoiced')  # Field name made lowercase.
    unit_of_measure = models.CharField(db_column='Unit_of_Measure', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unit_price = models.IntegerField(db_column='Unit_price')  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount')  # Field name made lowercase.
    lot_no_field = models.CharField(db_column='Lot_No_', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    expiry_date = models.DateTimeField(db_column='Expiry_date')  # Field name made lowercase.
    completed = models.IntegerField(db_column='Completed')  # Field name made lowercase.
    package_code = models.CharField(db_column='Package_Code', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'NewNovBills'