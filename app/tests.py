from django.test import TestCase
import pandas as pd
import pickle
import numpy as np
import os
from django.conf import settings

# Create your tests here.
# loading model
model_path = os.path.join(settings.BASE_DIR, 'app/models/diabetes.pkl')
with open(model_path, 'rb') as model_file:
    diabetes_model = pickle.load(model_file)
# diabetes function
def diabetespredict(Pregnancies,Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,DPF,Age):
    input_data=[Pregnancies,Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,DPF,Age]
    df = pd.DataFrame(input_data)
    final=np.asarray(df)
    final= final.reshape(1,-1)
    prediction=diabetes_model.predict(final)
    output='Patient is Diabetic' if prediction[0] else 'Patient is non Diabetic'
    return output
# loading model
model_path1 = os.path.join(settings.BASE_DIR, 'app/models/liver.pkl')
with open(model_path1, 'rb') as model_file1:
    liver_model = pickle.load(model_file1)
# liver function
def liverpredict(Age,Gender,BMI,Alcohol,Smoking,Genetic_risk,Physical_activity,Diabetes,Hypertension,Liver_function_test):
    input_data=[Age,Gender,BMI,Alcohol,Smoking,Genetic_risk,Physical_activity,Diabetes,Hypertension,Liver_function_test]
    df = pd.DataFrame(input_data)
    final=np.asarray(df)
    final= final.reshape(1,-1)
    prediction=liver_model.predict(final)
    output='Patient has liver disease' if prediction[0] else "Patient don't have liver disease"
    return output
# loading model
model_path2 = os.path.join(settings.BASE_DIR, 'app/models/heart.pkl')    
with open(model_path2, 'rb') as model_file2:
    heart_model = pickle.load(model_file2)
# heart function
def heartpredict(Age,Sex,chest_pain_type,resting_bp,cholesterol,fasting_blood_sugar,resting_ecg,max_heart_rate,exercise_angina,oldpeak,st_slope):
    input_data=[Age,Sex,chest_pain_type,resting_bp,cholesterol,fasting_blood_sugar,resting_ecg,max_heart_rate,exercise_angina,oldpeak,st_slope]
    df = pd.DataFrame(input_data)
    final=np.asarray(df)
    final= final.reshape(1,-1)
    prediction=heart_model.predict(final)
    output='Patient has the risk of heart attack' if prediction[0] else "Patient is safe from heart attack"
    return output
# loading model
model_path3 = os.path.join(settings.BASE_DIR, 'app/models/brain.pkl')    
with open(model_path3, 'rb') as model_file3:
    brain_model = pickle.load(model_file3)
# brain function
def brainpredict(Age,Gender,Ethnicity,Education,BMI,Smoking,Alcohol,Physical_activity,Diet,Sleep,Family_history,CardiovascularDisease,Diabetes,Depression,HeadInjury,Hypertension,SystolicBP,DiastolicBP,CholesterolTotal,CholesterolLDL,CholesterolHDL,CholesterolTriglycerides,MMSE,FunctionalAssessment,Memory_comp,Behaviour,Adl,confusion,disorientation,personalityChanges,difficultyCompletingTasks,forgetfulness):
    input_data=[Age,Gender,Ethnicity,Education,BMI,Smoking,Alcohol,Physical_activity,Diet,Sleep,Family_history,CardiovascularDisease,Diabetes,Depression,HeadInjury,Hypertension,SystolicBP,DiastolicBP,CholesterolTotal,CholesterolLDL,CholesterolHDL,CholesterolTriglycerides,MMSE,FunctionalAssessment,Memory_comp,Behaviour,Adl,confusion,disorientation,personalityChanges,difficultyCompletingTasks,forgetfulness]
    df = pd.DataFrame(input_data)
    final=np.asarray(df)
    final= final.reshape(1,-1)
    prediction=brain_model.predict(final)
    output='Patient has alzheimers' if prediction[0] else "Patient don't have alzheimers"
    return output 


# loading model
model_path4 = os.path.join(settings.BASE_DIR, 'app/models/asthama.pkl')    
with open(model_path4, 'rb') as model_file4:
    lungs_model = pickle.load(model_file4)
# brain function
def lungspredict(age,gender,ethnicity,educationLevel,bmi,smoking,physicalActivity,dietQuality,sleepQuality,pollutionExposure,pollenExposure,dustExposure,petAllergy,familyHistoryAsthma,historyOfAllergies,eczema,hayFever,gastroesophagealReflux,lungFunctionFEV1,lungFunctionFVC,wheezing,shortnessOfBreath,chestTightness,coughing,nighttimeSymptoms,exerciseInduced):
    input_data=[age,gender,ethnicity,educationLevel,bmi,smoking,physicalActivity,dietQuality,sleepQuality,pollutionExposure,pollenExposure,dustExposure,petAllergy,familyHistoryAsthma,historyOfAllergies,eczema,hayFever,gastroesophagealReflux,lungFunctionFEV1,lungFunctionFVC,wheezing,shortnessOfBreath,chestTightness,coughing,nighttimeSymptoms,exerciseInduced]
    df = pd.DataFrame(input_data)
    final=np.asarray(df)
    final= final.reshape(1,-1)
    prediction=lungs_model.predict(final)
    output='Patient has asthama' if prediction[0] else "Patient don't have asthama"
    return output  


# loading model
model_path5 = os.path.join(settings.BASE_DIR, 'app/models/kidney.pkl')    
with open(model_path5, 'rb') as model_file5:
    kidney_model = pickle.load(model_file5)
# brain function
def kidneypredict(age,gender,ethnicity,socioeconomicStatus,educationLevel,bmi,smoking,alcoholConsumption,physicalActivity,dietQuality,sleepQuality,familyHistoryKidneyDisease,familyHistoryHypertension,familyHistoryDiabetes,previousAcuteKidneyInjury,urinaryTractInfections,systolicBP,diastolicBP,fastingBloodSugar,hba1c,serumCreatinine,bunLevels,gfr,proteinInUrine,acr,serumElectrolytesSodium,serumElectrolytesPotassium,serumElectrolytesCalcium,serumElectrolytesPhosphorus,hemoglobinLevels,cholesterolTotal,cholesterolLDL,cholesterolHDL,cholesterolTriglycerides,aceInhibitors,diuretics,nsaidsUse,statins,antidiabeticMedications,edema,fatigueLevels,nauseaVomiting,muscleCramps,itching,qualityOfLifeScore,heavyMetalsExposure,occupationalExposureChemicals,waterQuality,medicalCheckupsFrequency,medicationAdherence,healthLiteracy
):
    input_data=[age,gender,ethnicity,socioeconomicStatus,educationLevel,bmi,smoking,alcoholConsumption,physicalActivity,dietQuality,sleepQuality,familyHistoryKidneyDisease,familyHistoryHypertension,familyHistoryDiabetes,previousAcuteKidneyInjury,urinaryTractInfections,systolicBP,diastolicBP,fastingBloodSugar,hba1c,serumCreatinine,bunLevels,gfr,proteinInUrine,acr,serumElectrolytesSodium,serumElectrolytesPotassium,serumElectrolytesCalcium,serumElectrolytesPhosphorus,hemoglobinLevels,cholesterolTotal,cholesterolLDL,cholesterolHDL,cholesterolTriglycerides,aceInhibitors,diuretics,nsaidsUse,statins,antidiabeticMedications,edema,fatigueLevels,nauseaVomiting,muscleCramps,itching,qualityOfLifeScore,heavyMetalsExposure,occupationalExposureChemicals,waterQuality,medicalCheckupsFrequency,medicationAdherence,healthLiteracy
    ]
    df = pd.DataFrame(input_data)
    final=np.asarray(df)
    final= final.reshape(1,-1)
    prediction=kidney_model.predict(final)
    output='Patient has Chronic kidney' if prediction[0] else "Patient don't have Chronic kidney"
    return output  