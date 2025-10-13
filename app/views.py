from django.shortcuts import render
from app import tests

# Create your views here.
def index(request):
    return render(request,'index.html')
def diabetes(request):
    return render(request,'diabetes.html')
def brain(request):
    return render(request,'brain.html')
def lungs(request):
    return render(request,'lungs.html')
def kidney(request):
    return render(request,'kidney.html')
def heart(request):
    return render(request,'heart.html')
def liver(request):
    return render(request,'liver.html')
# diabetes
def dia_predict(request):
    if request.method=='POST':
        Pregnancies=request.POST.get('Pregnancies')
        Glucose=request.POST.get('Glucose')
        Blood_Pressure=request.POST.get('Blood_Pressure')
        Skin_Thickness=request.POST.get('Skin_Thickness')
        Insulin=request.POST.get('Insulin')
        BMI=request.POST.get('BMI')
        DPF=request.POST.get('DPF')
        Age=request.POST.get('Age')
        diabetes_output=tests.diabetespredict(Pregnancies,Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,DPF,Age)
    context={
        "diabetes_Result":f"{diabetes_output}"
    }
    return render(request,'diabetes.html',context)
# liver disease
def liver_predict(request):
    if request.method=='POST':
        Age=request.POST.get('age')
        Gender=request.POST.get('gender')
        BMI=request.POST.get('bmi')
        Alcohol=request.POST.get('alcohol')
        Smoking=request.POST.get('smoking')
        Genetic_risk=request.POST.get('genetic-risk')
        Physical_activity=request.POST.get('physical-activity')
        Diabetes=request.POST.get('diabetes')
        Hypertension=request.POST.get('hypertension')
        Liver_function_test=request.POST.get('liver-function-test')
        liver_output=tests.liverpredict(Age,Gender,BMI,Alcohol,Smoking,Genetic_risk,Physical_activity,Diabetes,Hypertension,Liver_function_test)
    context={
        "liver_Result":f"{liver_output}"
    }
    return render(request,'liver.html',context)
# heart disease
def heart_predict(request):
    if request.method=='POST':
        Age=request.POST.get('age')
        Sex=request.POST.get('sex')
        chest_pain_type=request.POST.get('chest-pain-type')
        resting_bp=request.POST.get('resting-bp')
        cholesterol=request.POST.get('cholesterol')
        fasting_blood_sugar=request.POST.get('fasting-blood-sugar')
        resting_ecg=request.POST.get('resting-ecg')
        max_heart_rate=request.POST.get('max-heart-rate')
        exercise_angina=request.POST.get('exercise-angina')
        oldpeak=request.POST.get('oldpeak')
        st_slope=request.POST.get('st-slope')
        heart_output=tests.heartpredict(Age,Sex,chest_pain_type,resting_bp,cholesterol,fasting_blood_sugar,resting_ecg,max_heart_rate,exercise_angina,oldpeak,st_slope)
    context={
        "heart_Result":f"{heart_output}"
    }
    return render(request,'heart.html',context)
# brain disease
def brain_predict(request):
    if request.method=='POST':
        Age=request.POST.get('age')
        Gender=request.POST.get('gender')
        Ethnicity=request.POST.get('ethnicity')
        Education=request.POST.get('educationLevel')
        BMI=request.POST.get('bmi')
        Smoking=request.POST.get('smoking')
        Alcohol=request.POST.get('alcoholConsumption')
        Physical_activity=request.POST.get('physicalActivity')
        Diet=request.POST.get('dietQuality')
        Sleep=request.POST.get('sleepQuality')
        Family_history=request.POST.get('familyHistory')
        CardiovascularDisease=request.POST.get('CardiovascularDisease')
        Diabetes=request.POST.get('Diabetes')
        Depression=request.POST.get('Depression')
        HeadInjury=request.POST.get('HeadInjury')
        Hypertension=request.POST.get('Hypertension')
        SystolicBP=request.POST.get('SystolicBP')
        DiastolicBP=request.POST.get('DiastolicBP')
        CholesterolTotal=request.POST.get('CholesterolTotal')
        CholesterolLDL=request.POST.get('CholesterolLDL')
        CholesterolHDL=request.POST.get('CholesterolHDL')
        CholesterolTriglycerides=request.POST.get('CholesterolTriglycerides')
        MMSE=request.POST.get('MMSE')
        FunctionalAssessment=request.POST.get('FunctionalAssessment')
        Memory_comp=request.POST.get('memoryComplaints')
        Behaviour=request.POST.get('behavioralProblems')
        Adl=request.POST.get('adl')
        confusion=request.POST.get('confusion')
        disorientation=request.POST.get('disorientation')
        personalityChanges=request.POST.get('personalityChanges')
        difficultyCompletingTasks=request.POST.get('difficultyCompletingTasks')
        forgetfulness=request.POST.get('forgetfulness')
        brain_output=tests.brainpredict(Age,Gender,Ethnicity,Education,BMI,Smoking,Alcohol,Physical_activity,Diet,Sleep,Family_history,CardiovascularDisease,Diabetes,Depression,HeadInjury,Hypertension,SystolicBP,DiastolicBP,CholesterolTotal,CholesterolLDL,CholesterolHDL,CholesterolTriglycerides,MMSE,FunctionalAssessment,Memory_comp,Behaviour,Adl,confusion,disorientation,personalityChanges,difficultyCompletingTasks,forgetfulness)
    context={
        "brain_Result":f"{brain_output}"
    }
    return render(request,'brain.html',context)

# asthama prediction
def lungs_predict(request):
    if request.method=='POST':
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        ethnicity=request.POST.get('ethnicity')
        educationLevel=request.POST.get('educationLevel')
        bmi=request.POST.get('bmi')
        smoking=request.POST.get('smoking')
        physicalActivity=request.POST.get('physicalActivity')
        dietQuality=request.POST.get('dietQuality')
        sleepQuality=request.POST.get('sleepQuality')
        pollutionExposure=request.POST.get('pollutionExposure')
        pollenExposure=request.POST.get('pollenExposure')
        dustExposure=request.POST.get('dustExposure')
        petAllergy=request.POST.get('petAllergy')
        familyHistoryAsthma=request.POST.get('familyHistoryAsthma')
        historyOfAllergies=request.POST.get('historyOfAllergies')
        eczema=request.POST.get('eczema')
        hayFever=request.POST.get('hayFever')
        gastroesophagealReflux=request.POST.get('gastroesophagealReflux')
        lungFunctionFEV1=request.POST.get('lungFunctionFEV1')
        lungFunctionFVC=request.POST.get('lungFunctionFVC')
        wheezing=request.POST.get('wheezing')
        shortnessOfBreath=request.POST.get('shortnessOfBreath')
        chestTightness=request.POST.get('chestTightness')
        coughing=request.POST.get('coughing')
        nighttimeSymptoms=request.POST.get('nighttimeSymptoms')
        exerciseInduced=request.POST.get('exerciseInduced')
        lungs_output=tests.lungspredict(age,gender,ethnicity,educationLevel,bmi,smoking,physicalActivity,dietQuality,sleepQuality,pollutionExposure,pollenExposure,dustExposure,petAllergy,familyHistoryAsthma,historyOfAllergies,eczema,hayFever,gastroesophagealReflux,lungFunctionFEV1,lungFunctionFVC,wheezing,shortnessOfBreath,chestTightness,coughing,nighttimeSymptoms,exerciseInduced)
    context={
        "lungs_Result":f"{lungs_output}"
    }
    return render(request,'lungs.html',context)

# Kidney disease
def kidney_predict(request):
    if request.method=='POST':
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        ethnicity=request.POST.get('ethnicity')
        socioeconomicStatus=request.POST.get('socioeconomicStatus')
        educationLevel=request.POST.get('educationLevel')
        bmi=request.POST.get('bmi')
        smoking=request.POST.get('smoking')
        alcoholConsumption=request.POST.get('alcoholConsumption')
        physicalActivity=request.POST.get('physicalActivity')
        dietQuality=request.POST.get('dietQuality')
        sleepQuality=request.POST.get('sleepQuality')
        familyHistoryKidneyDisease=request.POST.get('familyHistoryKidneyDisease')
        familyHistoryHypertension=request.POST.get('familyHistoryHypertension')
        familyHistoryDiabetes=request.POST.get('familyHistoryDiabetes')
        previousAcuteKidneyInjury=request.POST.get('previousAcuteKidneyInjury')
        urinaryTractInfections=request.POST.get('urinaryTractInfections')
        systolicBP=request.POST.get('systolicBP')
        diastolicBP=request.POST.get('diastolicBP')
        fastingBloodSugar=request.POST.get('fastingBloodSugar')
        hba1c=request.POST.get('hba1c')
        serumCreatinine=request.POST.get('serumCreatinine')
        bunLevels=request.POST.get('bunLevels')
        gfr=request.POST.get('gfr')
        proteinInUrine=request.POST.get('proteinInUrine')
        acr=request.POST.get('acr')
        serumElectrolytesSodium=request.POST.get('serumElectrolytesSodium')
        serumElectrolytesPotassium=request.POST.get('serumElectrolytesPotassium')
        serumElectrolytesCalcium=request.POST.get('serumElectrolytesCalcium')
        serumElectrolytesPhosphorus=request.POST.get('serumElectrolytesPhosphorus')
        hemoglobinLevels=request.POST.get('hemoglobinLevels')
        cholesterolTotal=request.POST.get('cholesterolTotal')
        cholesterolLDL=request.POST.get('cholesterolLDL')
        cholesterolHDL=request.POST.get('cholesterolHDL')
        cholesterolTriglycerides=request.POST.get('cholesterolTriglycerides')
        aceInhibitors=request.POST.get('aceInhibitors')
        diuretics=request.POST.get('diuretics')
        nsaidsUse=request.POST.get('nsaidsUse')
        statins=request.POST.get('statins')
        antidiabeticMedications=request.POST.get('antidiabeticMedications')
        edema=request.POST.get('edema')
        fatigueLevels=request.POST.get('fatigueLevels')
        nauseaVomiting=request.POST.get('nauseaVomiting')
        muscleCramps=request.POST.get('muscleCramps')
        itching=request.POST.get('itching')
        qualityOfLifeScore=request.POST.get('qualityOfLifeScore')
        heavyMetalsExposure=request.POST.get('heavyMetalsExposure')
        occupationalExposureChemicals=request.POST.get('occupationalExposureChemicals')
        waterQuality=request.POST.get('waterQuality')
        medicalCheckupsFrequency=request.POST.get('medicalCheckupsFrequency')
        medicationAdherence=request.POST.get('medicationAdherence')
        healthLiteracy=request.POST.get('healthLiteracy')
        kidney_output=tests.kidneypredict(age,gender,ethnicity,socioeconomicStatus,educationLevel,bmi,smoking,alcoholConsumption,physicalActivity,dietQuality,sleepQuality,familyHistoryKidneyDisease,familyHistoryHypertension,familyHistoryDiabetes,previousAcuteKidneyInjury,urinaryTractInfections,systolicBP,diastolicBP,fastingBloodSugar,hba1c,serumCreatinine,bunLevels,gfr,proteinInUrine,acr,serumElectrolytesSodium,serumElectrolytesPotassium,serumElectrolytesCalcium,serumElectrolytesPhosphorus,hemoglobinLevels,cholesterolTotal,cholesterolLDL,cholesterolHDL,cholesterolTriglycerides,aceInhibitors,diuretics,nsaidsUse,statins,antidiabeticMedications,edema,fatigueLevels,nauseaVomiting,muscleCramps,itching,qualityOfLifeScore,heavyMetalsExposure,occupationalExposureChemicals,waterQuality,medicalCheckupsFrequency,medicationAdherence,healthLiteracy
    )
    context={
        "kidney_Result":f"{kidney_output}"
    }
    return render(request,'kidney.html',context)


