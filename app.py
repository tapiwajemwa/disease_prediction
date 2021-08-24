from flask import Flask,render_template,request
import pickle
import pandas as pd


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=["GET","POST"])
def main():
    if request.method == 'GET':
        return(render_template('main.html'))

    if request.method == "POST":
        abdominal_pain = request.form.getlist("  abdominal_pain ")
        if request.form.getlist("  abdominal_pain ") == []:      abdominal_pain = ["0"]
        abnormal_menstruation = request.form.getlist("  abnormal_menstruation ")
        if request.form.getlist("  abnormal_menstruation ") == []:      abnormal_menstruation = ["0"]
        acidity = request.form.getlist("  acidity ")
        if request.form.getlist("  acidity ") == []:      acidity = ["0"]
        acute_liver_failure = request.form.getlist("  acute_liver_failure ")
        if request.form.getlist("  acute_liver_failure ") == []:      acute_liver_failure = ["0"]
        altered_sensorium = request.form.getlist("  altered_sensorium ")
        if request.form.getlist("  altered_sensorium ") == []:      altered_sensorium = ["0"]
        anxiety = request.form.getlist("  anxiety ")
        if request.form.getlist("  anxiety ") == []:      anxiety = ["0"]


        back_pain = request.form.getlist("  back_pain ")
        if request.form.getlist("  back_pain ") == []:      back_pain = ["0"]
        belly_pain = request.form.getlist("  belly_pain ")
        if request.form.getlist("  belly_pain ") == []:      belly_pain = ["0"]
        blackheads = request.form.getlist("  blackheads ")
        if request.form.getlist("  blackheads ") == []:      blackheads = ["0"]
        bladder_discomfort = request.form.getlist("  bladder_discomfort ")
        if request.form.getlist("  bladder_discomfort ") == []:      bladder_discomfort = ["0"]
        blister = request.form.getlist("  blister ")
        if request.form.getlist("  blister ") == []:      blister = ["0"]


        blood_in_sputum = request.form.getlist("  blood_in_sputum ")
        if request.form.getlist("  blood_in_sputum ") == []:      blood_in_sputum = ["0"]
        bloody_stool = request.form.getlist("  bloody_stool ")
        if request.form.getlist("  bloody_stool ") == []:      bloody_stool = ["0"]
        blurred_and_distorted_vision = request.form.getlist("  blurred_and_distorted_vision ")
        if request.form.getlist("  blurred_and_distorted_vision ") == []:      blurred_and_distorted_vision = ["0"]
        breathlessness = request.form.getlist("  breathlessness ")
        if request.form.getlist("  breathlessness ") == []:      breathlessness = ["0"]
        brittle_nails = request.form.getlist("  brittle_nails ")
        if request.form.getlist("  brittle_nails ") == []:      brittle_nails = ["0"]


        bruising = request.form.getlist("  bruising ")
        if request.form.getlist("  bruising ") == []:      bruising = ["0"]
        burning_micturition = request.form.getlist("  burning_micturition ")
        if request.form.getlist("  burning_micturition ") == []:      burning_micturition = ["0"]
        chest_pain = request.form.getlist("  chest_pain ")
        if request.form.getlist("  chest_pain ") == []:      chest_pain = ["0"]
        chills = request.form.getlist("  chills ")
        if request.form.getlist("  chills ") == []:      chills = ["0"]
        cold_hands_and_feets = request.form.getlist("  cold_hands_and_feets ")
        if request.form.getlist("  cold_hands_and_feets ") == []:      cold_hands_and_feets = ["0"]


        coma = request.form.getlist("  coma ")
        if request.form.getlist("  coma ") == []:      coma = ["0"]
        congestion = request.form.getlist("  congestion ")
        if request.form.getlist("  congestion ") == []:      congestion = ["0"]
        constipation = request.form.getlist("  constipation ")
        if request.form.getlist("  constipation ") == []:      constipation = ["0"]
        continuous_feel_of_urine = request.form.getlist("  continuous_feel_of_urine ")
        if request.form.getlist("  continuous_feel_of_urine ") == []:      continuous_feel_of_urine = ["0"]
        continuous_sneezing = request.form.getlist("  continuous_sneezing ")
        if request.form.getlist("  continuous_sneezing ") == []:      continuous_sneezing = ["0"]


        cough = request.form.getlist("  cough ")
        if request.form.getlist("  cough ") == []:      cough = ["0"]
        cramps = request.form.getlist("  cramps ")
        if request.form.getlist("  cramps ") == []:      cramps = ["0"]
        dark_urine = request.form.getlist("  dark_urine ")
        if request.form.getlist("  dark_urine ") == []:      dark_urine = ["0"]
        dehydration = request.form.getlist("  dehydration ")
        if request.form.getlist("  dehydration ") == []:      dehydration = ["0"]
        depression = request.form.getlist("  depression ")
        if request.form.getlist("  depression ") == []:      depression = ["0"]


        diarrhoea = request.form.getlist("  diarrhoea ")
        if request.form.getlist("  diarrhoea ") == []:      diarrhoea = ["0"]
        dischromic_patches = request.form.getlist("  dischromic _patches ")
        if request.form.getlist("  dischromic _patches ") == []:      dischromic_patches = ["0"]
        distention_of_abdomen = request.form.getlist("  distention_of_abdomen ")
        if request.form.getlist("  distention_of_abdomen ") == []:      distention_of_abdomen = ["0"]
        dizziness = request.form.getlist("  dizziness ")
        if request.form.getlist("  dizziness ") == []:      dizziness = ["0"]
        drying_and_tingling_lips = request.form.getlist("  drying_and_tingling_lips ")
        if request.form.getlist("  drying_and_tingling_lips ") == []:      drying_and_tingling_lips = ["0"]


        enlarged_thyroid = request.form.getlist("  enlarged_thyroid ")
        if request.form.getlist("  enlarged_thyroid ") == []:      enlarged_thyroid = ["0"]
        excessive_hunger = request.form.getlist("  excessive_hunger ")
        if request.form.getlist("  excessive_hunger ") == []:      excessive_hunger = ["0"]
        extra_marital_contacts = request.form.getlist("  extra_marital_contacts ")
        if request.form.getlist("  extra_marital_contacts ") == []:      extra_marital_contacts = ["0"]
        family_history = request.form.getlist("  family_history ")
        if request.form.getlist("  family_history ") == []:      family_history = ["0"]
        fast_heart_rate = request.form.getlist("  fast_heart_rate ")
        if request.form.getlist("  fast_heart_rate ") == []:      fast_heart_rate = ["0"]


        fatigue = request.form.getlist("  fatigue ")
        if request.form.getlist("  fatigue ") == []:      fatigue = ["0"]
        fluid_overload = request.form.getlist("  fluid_overload ")
        if request.form.getlist("  fluid_overload ") == []:      fluid_overload = ["0"]
        foul_smell_of_urine = request.form.getlist("  foul_smell_of urine ")
        if request.form.getlist("  foul_smell_of urine ") == []:      foul_smell_of_urine = ["0"]
        headache = request.form.getlist("  headache ")
        if request.form.getlist("  headache ") == []:      headache = ["0"]
        high_fever = request.form.getlist("  high_fever ")
        if request.form.getlist("  high_fever ") == []:      high_fever = ["0"]


        hip_joint_pain = request.form.getlist("  hip_joint_pain ")
        if request.form.getlist("  hip_joint_pain ") == []:      hip_joint_pain = ["0"]
        history_of_alcohol_consumption = request.form.getlist("  history_of_alcohol_consumption ")
        if request.form.getlist("  history_of_alcohol_consumption ") == []:      history_of_alcohol_consumption = ["0"]
        increased_appetite = request.form.getlist("  increased_appetite ")
        if request.form.getlist("  increased_appetite ") == []:      increased_appetite = ["0"]
        indigestion = request.form.getlist("  indigestion ")
        if request.form.getlist("  indigestion ") == []:      indigestion = ["0"]
        inflammatory_nails = request.form.getlist("  inflammatory_nails ")
        if request.form.getlist("  inflammatory_nails ") == []:      inflammatory_nails = ["0"]


        internal_itching = request.form.getlist("  internal_itching ")
        if request.form.getlist("  internal_itching ") == []:      internal_itching = ["0"]
        irregular_sugar_level = request.form.getlist("  irregular_sugar_level ")
        if request.form.getlist("  irregular_sugar_level ") == []:      irregular_sugar_level = ["0"]
        irritability = request.form.getlist("  irritability ")
        if request.form.getlist("  irritability ") == []:      irritability = ["0"]
        irritation_in_anus = request.form.getlist("  irritation_in_anus ")
        if request.form.getlist("  irritation_in_anus ") == []:      irritation_in_anus = ["0"]
        itching = request.form.getlist("  itching ")
        if request.form.getlist("  itching ") == []:      itching = ["0"]


        joint_pain = request.form.getlist("  joint_pain ")
        if request.form.getlist("  joint_pain ") == []:      joint_pain = ["0"]
        knee_pain = request.form.getlist("  knee_pain ")
        if request.form.getlist("  knee_pain ") == []:      knee_pain = ["0"]
        lack_of_concentration = request.form.getlist("  lack_of_concentration ")
        if request.form.getlist("  lack_of_concentration ") == []:      lack_of_concentration = ["0"]
        lethargy = request.form.getlist("  lethargy ")
        if request.form.getlist("  lethargy ") == []:      lethargy = ["0"]
        lethargy_dizziness = request.form.getlist("  lethargy dizziness ")
        if request.form.getlist("  lethargy dizziness ") == []:      lethargy_dizziness = ["0"]


        loss_of_appetite = request.form.getlist("  loss_of_appetite ")
        if request.form.getlist("  loss_of_appetite ") == []:      loss_of_appetite = ["0"]
        loss_of_balance = request.form.getlist("  loss_of_balance ")
        if request.form.getlist("  loss_of_balance ") == []:      loss_of_balance = ["0"]
        loss_of_smell = request.form.getlist("  loss_of_smell ")
        if request.form.getlist("  loss_of_smell ") == []:      loss_of_smell = ["0"]
        malaise = request.form.getlist("  malaise ")
        if request.form.getlist("  malaise ") == []:      malaise = ["0"]
        mild_fever = request.form.getlist("  mild_fever ")
        if request.form.getlist("  mild_fever ") == []:      mild_fever = ["0"]


        mood_swings = request.form.getlist("  mood_swings ")
        if request.form.getlist("  mood_swings ") == []:      mood_swings = ["0"]
        movement_stiffness = request.form.getlist("  movement_stiffness ")
        if request.form.getlist("  movement_stiffness ") == []:      movement_stiffness = ["0"]
        mucoid_sputum = request.form.getlist("  mucoid_sputum ")
        if request.form.getlist("  mucoid_sputum ") == []:      mucoid_sputum = ["0"]
        muscle_pain = request.form.getlist("  muscle_pain ")
        if request.form.getlist("  muscle_pain ") == []:      muscle_pain = ["0"]
        muscle_pain_receiving_blood_transfusion = request.form.getlist("  muscle_pain receiving_blood_transfusion ")
        if request.form.getlist("  muscle_pain receiving_blood_transfusion ") == []:      muscle_pain_receiving_blood_transfusion = ["0"]


        muscle_wasting = request.form.getlist("  muscle_wasting ")
        if request.form.getlist("  muscle_wasting ") == []:      muscle_wasting = ["0"]
        muscle_weakness = request.form.getlist("  muscle_weakness ")
        if request.form.getlist("  muscle_weakness ") == []:      muscle_weakness = ["0"]
        nausea = request.form.getlist("  nausea ")
        if request.form.getlist("  nausea ") == []:      nausea = ["0"]
        neck_pain = request.form.getlist("  neck_pain ")
        if request.form.getlist("  neck_pain ") == []:      neck_pain = ["0"]
        nodal_skin_eruptions = request.form.getlist("  nodal_skin_eruptions ")
        if request.form.getlist("  nodal_skin_eruptions ") == []:      nodal_skin_eruptions = ["0"]


        obesity = request.form.getlist("  obesity ")
        if request.form.getlist("  obesity ") == []:      obesity = ["0"]
        pain_behind_the_eyes = request.form.getlist("  pain_behind_the_eyes ")
        if request.form.getlist("  pain_behind_the_eyes ") == []:      pain_behind_the_eyes = ["0"]
        pain_during_bowel_movements = request.form.getlist("  pain_during_bowel_movements ")
        if request.form.getlist("  pain_during_bowel_movements ") == []:      pain_during_bowel_movements = ["0"]
        pain_in_anal_region = request.form.getlist("  pain_in_anal_region ")
        if request.form.getlist("  pain_in_anal_region ") == []:      pain_in_anal_region = ["0"]
        painful_walking = request.form.getlist("  painful_walking ")
        if request.form.getlist("  painful_walking ") == []:      painful_walking = ["0"]


        palpitations = request.form.getlist("  palpitations ")
        if request.form.getlist("  palpitations ") == []:      palpitations = ["0"]
        passage_of_gases = request.form.getlist("  passage_of_gases ")
        if request.form.getlist("  passage_of_gases ") == []:      passage_of_gases = ["0"]
        patches_in_throat = request.form.getlist("  patches_in_throat ")
        if request.form.getlist("  patches_in_throat ") == []:      patches_in_throat = ["0"]
        phlegm = request.form.getlist("  phlegm ")
        if request.form.getlist("  phlegm ") == []:      phlegm = ["0"]
        polyuria = request.form.getlist("  polyuria ")
        if request.form.getlist("  polyuria ") == []:      polyuria = ["0"]


        prominent_veins_on_calf = request.form.getlist("  prominent_veins_on_calf ")
        if request.form.getlist("  prominent_veins_on_calf ") == []:      prominent_veins_on_calf = ["0"]
        puffy_face_and_eyes = request.form.getlist("  puffy_face_and_eyes ")
        if request.form.getlist("  puffy_face_and_eyes ") == []:      puffy_face_and_eyes = ["0"]
        pus_filled_pimples = request.form.getlist("  pus_filled_pimples ")
        if request.form.getlist("  pus_filled_pimples ") == []:      pus_filled_pimples = ["0"]
        receiving_blood_transfusion = request.form.getlist("  receiving_blood_transfusion ")
        if request.form.getlist("  receiving_blood_transfusion ") == []:      receiving_blood_transfusion = ["0"]
        receiving_unsterile_injections = request.form.getlist("  receiving_unsterile_injections ")
        if request.form.getlist("  receiving_unsterile_injections ") == []:      receiving_unsterile_injections = ["0"]


        red_sore_around_nose = request.form.getlist("  red_sore_around_nose ")
        if request.form.getlist("  red_sore_around_nose ") == []:      red_sore_around_nose = ["0"]
        red_spots_over_body = request.form.getlist("  red_spots_over_body ")
        if request.form.getlist("  red_spots_over_body ") == []:      red_spots_over_body = ["0"]
        redness_of_eyes = request.form.getlist("  redness_of_eyes ")
        if request.form.getlist("  redness_of_eyes ") == []:      redness_of_eyes = ["0"]
        restlessness = request.form.getlist("  restlessness ")
        if request.form.getlist("  restlessness ") == []:      restlessness = ["0"]
        runny_nose = request.form.getlist("  runny_nose ")
        if request.form.getlist("  runny_nose ") == []:      runny_nose = ["0"]


        rusty_sputum = request.form.getlist("  rusty_sputum ")
        if request.form.getlist("  rusty_sputum ") == []:      rusty_sputum = ["0"]
        scurring = request.form.getlist("  scurring ")
        if request.form.getlist("  scurring ") == []:      scurring = ["0"]
        shivering = request.form.getlist("  shivering ")
        if request.form.getlist("  shivering ") == []:      shivering = ["0"]
        silver_like_dusting = request.form.getlist("  silver_like_dusting ")
        if request.form.getlist("  silver_like_dusting ") == []:      silver_like_dusting = ["0"]
        sinus_pressure = request.form.getlist("  sinus_pressure ")
        if request.form.getlist("  sinus_pressure ") == []:      sinus_pressure = ["0"]


        skin_peeling = request.form.getlist("  skin_peeling ")
        if request.form.getlist("  skin_peeling ") == []:      skin_peeling = ["0"]
        skin_rash = request.form.getlist("  skin_rash ")
        if request.form.getlist("  skin_rash ") == []:      skin_rash = ["0"]
        slurred_speech = request.form.getlist("  slurred_speech ")
        if request.form.getlist("  slurred_speech ") == []:      slurred_speech = ["0"]
        small_dents_in_nails = request.form.getlist("  small_dents_in_nails ")
        if request.form.getlist("  small_dents_in_nails ") == []:      small_dents_in_nails = ["0"]
        spinning_movements = request.form.getlist("  spinning_movements ")
        if request.form.getlist("  spinning_movements ") == []:      spinning_movements = ["0"]


        spotting_urination = request.form.getlist("  spotting_ urination ")
        if request.form.getlist("  spotting_ urination ") == []:      spotting_urination = ["0"]
        spotting_urination1 = request.form.getlist("  spotting_urination ")
        if request.form.getlist("  spotting_urination ") == []:      spotting_urination1 = ["0"]
        stiff_neck = request.form.getlist("  stiff_neck ")
        if request.form.getlist("  stiff_neck ") == []:      stiff_neck = ["0"]
        stomach_bleeding = request.form.getlist("  stomach_bleeding ")
        if request.form.getlist("  stomach_bleeding ") == []:      stomach_bleeding = ["0"]
        stomach_pain = request.form.getlist("  stomach_pain ")
        if request.form.getlist("  stomach_pain ") == []:      stomach_pain = ["0"]


        sunken_eyes = request.form.getlist("  sunken_eyes ")
        if request.form.getlist("  sunken_eyes ") == []:      sunken_eyes = ["0"]
        sweating = request.form.getlist("  sweating ")
        if request.form.getlist("  sweating ") == []:      sweating = ["0"]
        swelled_lymph_nodes = request.form.getlist("  swelled_lymph_nodes ")
        if request.form.getlist("  swelled_lymph_nodes ") == []:      swelled_lymph_nodes = ["0"]
        swelling_joints = request.form.getlist("  swelling_joints ")
        if request.form.getlist("  swelling_joints ") == []:      swelling_joints = ["0"]
        swelling_of_stomach = request.form.getlist("  swelling_of_stomach ")
        if request.form.getlist("  swelling_of_stomach ") == []:      swelling_of_stomach = ["0"]


        swollen_blood_vessels = request.form.getlist("  swollen_blood_vessels ")
        if request.form.getlist("  swollen_blood_vessels ") == []:      swollen_blood_vessels = ["0"]
        swollen_extremeties = request.form.getlist("  swollen_extremeties ")
        if request.form.getlist("  swollen_extremeties ") == []:      swollen_extremeties = ["0"]
        swollen_legs = request.form.getlist("  swollen_legs ")
        if request.form.getlist("  swollen_legs ") == []:      swollen_legs = ["0"]
        throat_irritation = request.form.getlist("  throat_irritation ")
        if request.form.getlist("  throat_irritation ") == []:      throat_irritation = ["0"]
        toxic_look = request.form.getlist("  toxic_look_(typhos) ")
        if request.form.getlist("  toxic_look_(typhos) ") == []:      toxic_look = ["0"]


        ulcers_on_tongue = request.form.getlist("  ulcers_on_tongue ")
        if request.form.getlist("  ulcers_on_tongue ") == []:      ulcers_on_tongue = ["0"]
        unsteadiness = request.form.getlist("  unsteadiness ")
        if request.form.getlist("  unsteadiness ") == []:      unsteadiness = ["0"]
        visual_disturbances = request.form.getlist("  visual_disturbances ")
        if request.form.getlist("  visual_disturbances ") == []:      visual_disturbances = ["0"]
        vomiting = request.form.getlist("  vomiting ")
        if request.form.getlist("  vomiting ") == []:      vomiting = ["0"]
        watering_from_eyes = request.form.getlist("  watering_from_eyes ")
        if request.form.getlist("  watering_from_eyes ") == []:      watering_from_eyes = ["0"]


        weakness_in_limbs = request.form.getlist("  weakness_in_limbs ")
        if request.form.getlist("  weakness_in_limbs ") == []:      weakness_in_limbs = ["0"]
        weakness_of_one_body_side = request.form.getlist("  weakness_of_one_body_side ")
        if request.form.getlist("  weakness_of_one_body_side ") == []:      weakness_of_one_body_side = ["0"]
        weight_gain = request.form.getlist("  weight_gain ")
        if request.form.getlist("  weight_gain ") == []:      weight_gain = ["0"]
        weight_loss = request.form.getlist("  weight_loss ")
        if request.form.getlist("  weight_loss ") == []:      weight_loss = ["0"]
        yellow_crust_ooze = request.form.getlist("  yellow_crust_ooze ")
        if request.form.getlist("  yellow_crust_ooze ") == []:      yellow_crust_ooze = ["0"]


        yellow_urine = request.form.getlist("  yellow_urine ")
        if request.form.getlist("  yellow_urine ") == []:      yellow_urine = ["0"]
        yellowing_of_eyes = request.form.getlist("  yellowing_of_eyes ")
        if request.form.getlist("  yellowing_of_eyes ") == []:      yellowing_of_eyes = ["0"]
        yellowish_skin = request.form.getlist("  yellowish_skin ")
        if request.form.getlist("  yellowish_skin ") == []:      yellowish_skin = ["0"]

        Columns=[' abdominal_pain', ' abnormal_menstruation', ' acidity', ' acute_liver_failure', ' altered_sensorium', ' anxiety', 
        ' back_pain', ' belly_pain', ' blackheads', ' bladder_discomfort', ' blister', ' blood_in_sputum', ' bloody_stool', ' blurred_and_distorted_vision', ' breathlessness', 
        ' brittle_nails', ' bruising', ' burning_micturition', ' chest_pain', ' chills', ' cold_hands_and_feets', ' coma', ' congestion', ' constipation', ' continuous_feel_of_urine', 
        ' continuous_sneezing', ' cough', ' cramps', ' dark_urine', ' dehydration', ' depression', ' diarrhoea', ' dischromic _patches', ' distention_of_abdomen', ' dizziness', 
        ' drying_and_tingling_lips', ' enlarged_thyroid', ' excessive_hunger', ' extra_marital_contacts', ' family_history', ' fast_heart_rate', ' fatigue', ' fluid_overload', 
        ' foul_smell_of urine', ' headache', ' high_fever', ' hip_joint_pain', ' history_of_alcohol_consumption', ' increased_appetite', ' indigestion', ' inflammatory_nails', 
        ' internal_itching', ' irregular_sugar_level', ' irritability', ' irritation_in_anus', ' itching', ' joint_pain', ' knee_pain', ' lack_of_concentration', ' lethargy', 
        ' lethargy dizziness', ' loss_of_appetite', ' loss_of_balance', ' loss_of_smell', ' malaise', ' mild_fever', ' mood_swings', ' movement_stiffness', ' mucoid_sputum', 
        ' muscle_pain', ' muscle_pain receiving_blood_transfusion', ' muscle_wasting', ' muscle_weakness', ' nausea', ' neck_pain', ' nodal_skin_eruptions', ' obesity', 
        ' pain_behind_the_eyes', ' pain_during_bowel_movements', ' pain_in_anal_region', ' painful_walking', ' palpitations', ' passage_of_gases', ' patches_in_throat', 
        ' phlegm', ' polyuria', ' prominent_veins_on_calf', ' puffy_face_and_eyes', ' pus_filled_pimples', ' receiving_blood_transfusion', ' receiving_unsterile_injections', 
        ' red_sore_around_nose', ' red_spots_over_body', ' redness_of_eyes', ' restlessness', ' runny_nose', ' rusty_sputum', ' scurring', ' shivering', ' silver_like_dusting', 
        ' sinus_pressure', ' skin_peeling', ' skin_rash', ' slurred_speech', ' small_dents_in_nails', ' spinning_movements', ' spotting_ urination', ' spotting_urination', 
        ' stiff_neck', ' stomach_bleeding', ' stomach_pain', ' sunken_eyes', ' sweating', ' swelled_lymph_nodes', ' swelling_joints', ' swelling_of_stomach', ' swollen_blood_vessels', 
        ' swollen_extremeties', ' swollen_legs', ' throat_irritation', ' toxic_look_(typhos)', ' ulcers_on_tongue', ' unsteadiness', ' visual_disturbances', ' vomiting', ' watering_from_eyes', 
        ' weakness_in_limbs', ' weakness_of_one_body_side', ' weight_gain', ' weight_loss', ' yellow_crust_ooze', ' yellow_urine', ' yellowing_of_eyes', ' yellowish_skin']

        data = [abdominal_pain[0], int(abnormal_menstruation[0]), int(acidity[0]), int(acute_liver_failure[0]), int(altered_sensorium[0]), int(anxiety[0]),
         int(back_pain[0]), int(belly_pain[0]), int(blackheads[0]), int(bladder_discomfort[0]), int(blister[0]), int(blood_in_sputum[0]), int(bloody_stool[0]), int(blurred_and_distorted_vision[0]), 
         int(breathlessness[0]), int(brittle_nails[0]), int(bruising[0]), int(burning_micturition[0]), int(chest_pain[0]), int(chills[0]), int(cold_hands_and_feets[0]), int(coma[0]), int(congestion[0]), 
         int(constipation[0]), int(continuous_feel_of_urine[0]), int(continuous_sneezing[0]), int(cough[0]), int(cramps[0]), int(dark_urine[0]), int(dehydration[0]), int(depression[0]), int(diarrhoea[0]), 
         int(dischromic_patches[0]), int(distention_of_abdomen[0]), int(dizziness[0]), int(drying_and_tingling_lips[0]), int(enlarged_thyroid[0]), int(excessive_hunger[0]), int(extra_marital_contacts[0]), 
         int(family_history[0]), int(fast_heart_rate[0]), int(fatigue[0]), int(fluid_overload[0]), int(foul_smell_of_urine[0]), int(headache[0]), int(high_fever[0]), int(hip_joint_pain[0]), int(history_of_alcohol_consumption[0]), 
         int(increased_appetite[0]), int(indigestion[0]), int(inflammatory_nails[0]), int(internal_itching[0]), int(irregular_sugar_level[0]), int(irritability[0]), int(irritation_in_anus[0]), int(itching[0]), 
         int(joint_pain[0]), int(knee_pain[0]), int(lack_of_concentration[0]), int(lethargy[0]), int(lethargy_dizziness[0]), int(loss_of_appetite[0]), int(loss_of_balance[0]), int(loss_of_smell[0]), int(malaise[0]), 
         int(mild_fever[0]), int(mood_swings[0]), int(movement_stiffness[0]), int(mucoid_sputum[0]), int(muscle_pain[0]), int(muscle_pain_receiving_blood_transfusion[0]), int(muscle_wasting[0]), int(muscle_weakness[0]), 
         int(nausea[0]), int(neck_pain[0]), int(nodal_skin_eruptions[0]), int(obesity[0]), int(pain_behind_the_eyes[0]), int(pain_during_bowel_movements[0]), int(pain_in_anal_region[0]), int(painful_walking[0]), int(palpitations[0]), 
         int(passage_of_gases[0]), int(patches_in_throat[0]), int(phlegm[0]), int(polyuria[0]), int(prominent_veins_on_calf[0]), int(puffy_face_and_eyes[0]), int(pus_filled_pimples[0]), int(receiving_blood_transfusion[0]), 
         int(receiving_unsterile_injections[0]), int(red_sore_around_nose[0]), int(red_spots_over_body[0]), int(redness_of_eyes[0]), int(restlessness[0]), int(runny_nose[0]), int(rusty_sputum[0]), int(scurring[0]), int(shivering[0]), 
         int(silver_like_dusting[0]), int(sinus_pressure[0]), int(skin_peeling[0]), int(skin_rash[0]), int(slurred_speech[0]), int(small_dents_in_nails[0]), int(spinning_movements[0]), int(spotting_urination[0]), int(spotting_urination1[0]), int(stiff_neck[0]),
         int(stomach_bleeding[0]), int(stomach_pain[0]), int(sunken_eyes[0]), int(sweating[0]), int(swelled_lymph_nodes[0]), int(swelling_joints[0]), int(swelling_of_stomach[0]), int(swollen_blood_vessels[0]), int(swollen_extremeties[0]), 
         int(swollen_legs[0]), int(throat_irritation[0]), int(toxic_look[0]), int(ulcers_on_tongue[0]), int(unsteadiness[0]), int(visual_disturbances[0]), int(vomiting[0]), int(watering_from_eyes[0]), int(weakness_in_limbs[0]), 
         int(weakness_of_one_body_side[0]), int(weight_gain[0]), int(weight_loss[0]), int(yellow_crust_ooze[0]), int(yellow_urine[0]), int(yellowing_of_eyes[0]), int(yellowish_skin[0])]
     
        input_variables = pd.DataFrame([data],columns = Columns)
        model = pickle.load(open('model1.pkl','rb'))
        prediction = model.predict(input_variables)
        

        return render_template('main.html', pred=prediction[0])
        app.run(debug=True)
