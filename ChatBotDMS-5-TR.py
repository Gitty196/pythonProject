import re

# Helper function to clean and prepare the user input for matching
def clean_input(user_text):
    return re.findall(r'\b\w+\b', user_text.lower())

# Basic example of a simplified rule-based chatbot in Python
def eve(user_text):
    tokens = clean_input(user_text)

    # Define greetings
    greetings = {"hello", "hi", "greetings", "hey", "what's up", "what is up"}
    if any(token in tokens for token in greetings):
        return "Hello! I am EVE. Your personal assistant for your DSM-5-TR. What would you like to learn today?"

    # Disorder keywords and descriptions
    disorder_keywords = {
        # Neurodevelopmental disorders:
        "intellectual developmental disorder (intellectual disability)": {"intellectual", "developmental", "disability","disorder"},
        "global developmental delay": {"global", "developmental", "delay"},
        "unspecified intellectual disability (intellectual developmental disorder)": {"unspecified", "intellectual", "disability", "developmental", "disorder"},
        "language disorder": {"language", "disorder"},
        "speech sound disorder": {"speech", "sound", "disorder"},
        "childhood-onset fluency disorder (stuttering)": {"childhood-onset", "fluency", "disorder", "stuttering"},
        "pragmatic (social) communication disorder": {"pragmatic", "social", "communication", "disorder"},
        "autism spectrum disorder": {"autism", "spectrum", "disorder"},
        "attention-deficit/hyperactivity disorder (ADHD)": {"attention-deficit", "hyperactivity", "disorder", "adhd"},
        "specific learning disorder": {"specific", "learning", "disorder"},
        "developmental coordination disorder": {"developmental", "coordination", "disorder"},
        "stereotypic movement disorder": {"stereotypic", "movement", "disorder"},
        "tic disorder": {"tic", "disorder"},

        # Anxiety Disorders:
        "social anxiety disorder": {"social", "anxiety", "disorder"},
        "separation anxiety disorder": {"separation", "anxiety", "disorder"},
        "selective mutism": {"selective", "mutism"},
        "specific phobia": {"specific", "phobia"},
        "panic disorder": {"panic", "disorder"},
        "panic attack specifier": {"panic", "attack", "specifier"},
        "agoraphobia": {"agoraphobia"},
        "generalized anxiety disorder": {"generalized", "anxiety", "disorder"},
        "substance/medication-induced anxiety disorder": {"substance", "medication-induced", "anxiety", "disorder"},
        "anxiety disorder due to another medical condition": {"anxiety", "disorder", "medical", "condition"},
        "other specified anxiety disorder": {"other", "specified", "anxiety", "disorder"},
        "chronic depressive disorder": {"chronic", "depressive", "disorder"},
        "disruptive mood dysfunction": {"disruptive", "mood", "dysfunction"},
        "major depressive disorder": {"major", "depressive", "disorder"},
        "persistent depressive disorder (dysthymia)": {"persistent", "depressive", "dysthymia"},
        "premenstrual dysphoric disorder": {"premenstrual", "dysphoric", "disorder"},
        "substance/medication-induced depressive disorder": {"substance", "medication-induced", "depressive","disorder"},
        "depressive disorder due to another medical condition": {"depressive", "disorder", "medical", "condition"},
        "other specified depressive disorder": {"other", "specified", "depressive", "disorder"},
        "unspecified depressive disorder": {"unspecified", "depressive", "disorder"},

        # Schizophrenia and other Psychotic Disorders:
        "schizotypal (personality) disorder": {"schizotypal", "personality", "disorder"},
        "delusional disorder": {"delusional", "disorder"},
        "brief psychotic disorder": {"brief", "psychotic", "disorder"},
        "schizophreniform": {"schizophreniform"},
        "schizophrenia": {"schizophrenia"},
        "schizoaffective disorder": {"schizoaffective", "disorder"},
        "substance/medication-induced psychotic disorder": {"substance", "medication-induced", "psychotic", "disorder"},
        "psychotic disorder due to another medical condition": {"psychotic", "disorder", "medical", "condition"},
        "catatonia associated with another mental disorder (catatonia specifier)": {"catatonia", "mental", "disorder","specifier"},
        "catatonic disorder due to another medical condition": {"catatonic", "disorder", "medical", "condition"},
        "other specified schizophrenia spectrum and other psychotic disorder": {"other", "specified", "schizophrenia","psychotic", "disorder"},
        "unspecified schizophrenia spectrum and other psychotic disorder": {"unspecified", "schizophrenia", "psychotic","disorder"},
        "unspecified catatonia": {"unspecified", "catatonia"},

        # Bipolar Disorders and Related Disorders:
        "bipolar I (1) disorder": {"bipolar", "I", "1", "disorder"},
        "bipolar II (2) disorder": {"bipolar", "II", "2", "disorder"},
        "cyclothymic disorder": {"cyclothymic", "disorder"},
        "substance/medication-induced bipolar and related disorder": {"substance", "medication-induced", "bipolar","disorder"},
        "bipolar and related disorder due to another medical condition": {"bipolar", "disorder", "medical","condition"},
        "other specified bipolar and related disorder": {"other", "specified", "bipolar", "disorder"},
        "unspecified bipolar and related disorder": {"unspecified", "bipolar", "disorder"},

        # Obsessive-Compulsive Disorder (OCD):
        "obsessive-compulsive disorder (OCD)": {"obsessive", "compulsive", "disorder", "ocd"},
        "body dysmorphic disorder": {"body", "dysmorphic", "disorder"},
        "hoarding disorder": {"hoarding", "disorder"},
        "trichotillomania (hair-pulling disorder)": {"trichotillomania", "hair-pulling", "disorder"},
        "excoriation (skin-picking) disorder": {"excoriation", "skin-picking", "disorder"},
        "substance/medication-induced obsessive-compulsive and related disorder": {"substance", "medication-induced","obsessive-compulsive", "disorder"},
        "obsessive-compulsive and related disorder due to another medical condition": {"obsessive-compulsive","disorder", "medical","condition"},
        "other specified obsessive-compulsive and related disorder": {"other", "specified", "obsessive-compulsive","disorder"},
        "unspecified obsessive-compulsive and related disorder": {"unspecified", "obsessive-compulsive", "disorder"},

        # Trauma and Stressor-Related Disorders:
        "reactive attachment disorder": {"reactive", "attachment", "disorder"},
        "disinhibited social engagement disorder": {"disinhibited", "social", "engagement", "disorder"},
        "posttraumatic stress disorder (PTSD)": {"posttraumatic", "stress", "disorder", "ptsd"},
        "acute stress disorder": {"acute", "stress", "disorder"},
        "adjustment disorder": {"adjustment", "disorder"},
        "prolonged grief disorder": {"prolonged", "grief", "disorder"},
        "other specified trauma- and stressor-related disorder": {"other", "specified", "trauma", "stressor-related","disorder"},
        "unspecified trauma- and stressor-related disorder": {"unspecified", "trauma", "stressor-related", "disorder"},

        # Dissociative Disorders:
        "dissociative identity disorder": {"dissociative", "identity", "disorder"},
        "dissociative amnesia": {"dissociative", "amnesia"},
        "depersonalization/derealization disorder": {"depersonalization", "derealization", "disorder"},
        "other specified dissociative disorder": {"other", "specified", "dissociative", "disorder"},
        "unspecified dissociative disorder": {"unspecified", "dissociative", "disorder"},

        ##### Feeding and Eating Disorders:
        "pica": {"pica"},
        "rumination disorder": {"rumination", "disorder"},
        "avoidant/restrictive food intake disorder": {"avoidant", "restrictive", "food", "intake", "disorder"},
        "anorexia nervosa": {"anorexia", "nervosa"},
        "bulimia nervosa": {"bulimia", "nervosa"},
        "binge-eating disorder": {"binge-eating", "disorder"},
        "other specified feeding or eating disorder": {"other", "specified", "feeding", "eating", "disorder"},
        "unspecified feeding or eating disorder": {"unspecified", "feeding", "eating", "disorder"},

        # Elimination Disorders:
        "enuresis": {"enuresis"},
        "encopresis": {"encopresis"},
        "other specified elimination disorder": {"other", "specified", "elimination", "disorder"},
        "unspecified elimination disorder": {"unspecified", "elimination", "disorder"},

        # Sleep-Wake Disorders:
        "insomnia disorder": {"insomnia", "disorder"},
        "hypersomnolence disorder": {"hypersomnolence", "disorder"},
        "narcolepsy": {"narcolepsy"},
        "obstructive sleep apnea hypopnea": {"obstructive", "sleep", "apnea", "hypopnea"},
        "central sleep apnea": {"central", "sleep", "apnea"},
        "sleep-related hypoventilation": {"sleep-related", "hypoventilation"},
        "circadian rhythm sleep-wake disorder": {"circadian", "rhythm", "sleep-wake", "disorder"},
        "non-rapid eye movement (non-REM) sleep arousal": {"non-rapid", "eye", "movement", "non-rem", "sleep","arousal"},
        "nightmare disorder": {"nightmare", "disorder"},
        "rapid eye movement (REM) sleep behavior disorder": {"rapid", "eye", "movement", "rem", "sleep", "behavior","disorder"},
        "restless legs syndrome": {"restless", "legs", "syndrome"},
        "substance/medication-induced sleep disorder": {"substance", "medication-induced", "sleep", "disorder"},
        "other specified sleep-wake disorder": {"other", "specified", "sleep-wake", "disorder"},
        "unspecified sleep-wake disorder": {"unspecified", "sleep-wake", "disorder"},

        # Sexual Dysfunctions:
        "delayed ejaculation": {"delayed", "ejaculation"},
        "erectile disorder": {"erectile", "disorder"},
        "female orgasmic disorder": {"female", "orgasmic", "disorder"},
        "female sexual interest/arousal disorder": {"female", "sexual", "interest", "arousal", "disorder"},
        "genito-pelvic pain/penetration disorder": {"genito-pelvic", "pain", "penetration", "disorder"},
        "male hypoactive sexual desire disorder": {"male", "hypoactive", "sexual", "desire", "disorder"},
        "premature (early) ejaculation": {"premature", "early", "ejaculation"},
        "substance/medication-induced sexual disorder": {"substance", "medication-induced", "sexual", "disorder"},
        "other specified sexual dysfunction": {"other", "specified", "sexual", "dysfunction"},
        "unspecified sexual dysfunction": {"unspecified", "sexual", "dysfunction"},

        # Gender Dysphoria:
        "gender dysphoria in children": {"gender", "dysphoria", "children"},
        "gender dysphoria in adolescents and adults": {"gender", "dysphoria", "adolescents", "adults"},
        "other specified gender dysphoria": {"other", "specified", "gender", "dysphoria"},
        "unspecified gender dysphoria": {"unspecified", "gender", "dysphoria"},

        # Disruptive, Impulse-Control, and Conduct Disorders:
        "oppositional defiant disorder": {"oppositional", "defiant", "disorder"},
        "intermittent explosive disorder": {"intermittent", "explosive", "disorder"},
        "conduct disorder": {"conduct", "disorder"},
        "pyromania": {"pyromania"},
        "kleptomania": {"kleptomania"},
        "other specified disruptive, impulse-control, and conduct disorder": {"other", "specified", "disruptive", "impulse-control", "conduct", "disorder"},
        "unspecified disruptive, impulse-control, and conduct disorder": {"unspecified", "disruptive", "impulse-control", "conduct", "disorder"},

        # Substance-Related and Addicted Disorders:
        "alcohol-related disorders": {"alcohol", "related", "disorders"},
        "caffeine-related disorders": {"caffeine", "related", "disorders"},
        "cannabis-related disorders": {"cannabis", "related", "disorders"},
        "hallucinogen-related disorders": {"hallucinogen", "related", "disorders"},
        "inhalant-related disorders": {"inhalant", "related", "disorders"},
        "opioid-related disorders": {"opioid", "related", "disorders"},
        "sedative-, hypnotic-, or anxiolytic-related disorders": {"sedative", "hypnotic", "anxiolytic", "related", "disorders"},
        "stimulant-related disorders": {"stimulant", "related", "disorders"},
        "tobacco-related disorders": {"tobacco", "related", "disorders"},
        "other (or unknown) substance-related disorders": {"other", "unknown", "substance", "related", "disorders"},

        "alcohol use disorder": {"alcohol", "use", "disorder"},
        "alcohol intoxication": {"alcohol", "intoxication"},
        "alcohol withdrawal": {"alcohol", "withdrawal"},
        "caffeine intoxication": {"caffeine", "intoxication"},
        "caffeine withdrawal": {"caffeine", "withdrawal"},
        "cannabis use disorder": {"cannabis", "use", "disorder"},
        "cannabis intoxication": {"cannabis", "intoxication"},
        "cannabis withdrawal": {"cannabis", "withdrawal"},
        "phencyclidine (PCP) use disorder": {"phencyclidine", "pcp", "use", "disorder"},
        "other hallucinogen use disorder": {"hallucinogen", "use", "disorder"},
        "inhalant use disorder": {"inhalant", "use", "disorder"},
        "opioid use disorder": {"opioid", "use", "disorder"},
        "opioid intoxication": {"opioid", "intoxication"},
        "opioid withdrawal": {"opioid", "withdrawal"},
        "sedative, hypnotic, or anxiolytic use disorder": {"sedative", "hypnotic", "anxiolytic", "use", "disorder"},
        "stimulant use disorder": {"stimulant", "use", "disorder"},
        "tobacco use disorder": {"tobacco", "use", "disorder"},
        "gambling disorder": {"gambling", "disorder"},

        # Neurocognitive Disorders:
        "delirium": {"delirium"},
        "major neurocognitive disorder": {"major", "neurocognitive", "disorder"},
        "mild neurocognitive disorder": {"mild", "neurocognitive", "disorder"},
        "major or mild neurocognitive disorder due to Alzheimer's disease": {"major", "mild", "neurocognitive", "alzheimer's", "disease"},
        "major or mild frontotemporal neurocognitive disorder": {"major", "mild", "frontotemporal", "neurocognitive", "disorder"},
        "major or mild neurocognitive disorder with Lewy bodies": {"major", "mild", "neurocognitive", "lewy", "bodies"},
        "major or mild vascular neurocognitive disorder": {"major", "mild", "vascular", "neurocognitive", "disorder"},
        "major or mild neurocognitive disorder due to traumatic brain injury": {"major", "mild", "neurocognitive", "traumatic", "brain", "injury"},
        "substance/medication-induced major or mild neurocognitive disorder": {"substance", "medication-induced", "major", "mild", "neurocognitive", "disorder"},
        "major or mild neurocognitive disorder due to HIV infection": {"major", "mild", "neurocognitive", "hiv", "infection"},
        "major or mild neurocognitive disorder due to prion disease": {"major", "mild", "neurocognitive", "prion", "disease"},
        "major or mild neurocognitive disorder due to Parkinson's disease": {"major", "mild", "neurocognitive", "parkinson's", "disease"},
        "major or mild neurocognitive disorder due to Huntington's disease": {"major", "mild", "neurocognitive", "huntington's", "disease"},
        "major or mild neurocognitive disorder due to another medical condition": {"major", "mild", "neurocognitive", "medical", "condition"},
        "major or mild neurocognitive disorder due to multiple etiologies": {"major", "mild", "neurocognitive", "multiple", "etiologies"},
        "unspecified neurocognitive disorder": {"unspecified", "neurocognitive", "disorder"},

        # Additional Neurocognitive Conditions:
        "Alzheimer's disease": {"alzheimer's", "disease"},
        "frontotemporal degeneration": {"frontotemporal", "degeneration"},
        "Lewy body disease": {"lewy", "body", "disease"},
        "vascular disease": {"vascular", "disease"},
        "traumatic brain injury (TBI)": {"traumatic", "brain", "injury", "tbi"},
        "substance/medication use": {"substance", "medication", "use"},
        "HIV infection": {"hiv", "infection"},
        "prion disease": {"prion", "disease"},
        "Parkinson's disease": {"parkinson's", "disease"},
        "Huntington's disease": {"huntington's", "disease"},
        "multiple etiologies": {"multiple", "etiologies"},
        "unspecified etiology": {"unspecified", "etiology"},
        # Personality Disorders:
        "cluster A personality disorders": {"cluster", "a", "odd", "eccentric", "behavior", "paranoid", "schizoid","schizotypal", "personality", "disorders"},
        "cluster B personality disorders": {"cluster", "b", "dramatic", "emotional", "erratic", "behavior","antisocial", "borderline", "histrionic", "narcissistic", "personality","disorders"},
            "cluster C personality disorder": {"cluster", "c", "anxious", "fearful", "behavior", "avoidant","dependent", "obsessive-compulsive", "personality", "disorder"},

        # Cluster A Personality Disorders:
        "paranoid personality disorder": {"paranoid", "personality", "disorder"},
        "schizoid personality disorder": {"schizoid", "personality", "disorder"},
        "schizotypal personality disorder": {"schizotypal", "personality", "disorder"},

        # Cluster B Personality Disorders:
        "antisocial personality disorder": {"antisocial", "personality", "disorder"},
        "borderline personality disorder": {"borderline", "personality", "disorder"},
        "histrionic personality disorder": {"histrionic", "personality", "disorder"},
        "narcissistic personality disorder": {"narcissistic", "personality", "disorder"},

        # Cluster C Personality Disorders:
        "avoidant personality disorder": {"avoidant", "personality", "disorder"},
        "dependent personality disorder": {"dependent", "personality", "disorder"},
        "obsessive-compulsive personality disorder": {"obsessive-compulsive", "personality", "disorder"},

        # Other Personality Disorders:
        "personality change due to another medical condition": {"personality", "change", "medical", "condition"},
        "other specified personality disorder": {"other", "specified", "personality", "disorder"},
        "unspecified personality disorder": {"unspecified", "personality", "disorder"},

        # Paraphilic Disorders:
        "voyeuristic disorder": {"voyeuristic", "disorder"},
        "exhibitionist disorder": {"exhibitionist", "disorder"},
        "frotteuristic disorder": {"frotteuristic", "disorder"},
        "sexual masochism disorder": {"sexual", "masochism", "disorder"},
        "sexual sadism disorder": {"sexual", "sadism", "disorder"},
        "pedophilic disorder": {"pedophilic", "disorder"},
        "fetishistic disorder": {"fetishistic", "disorder"},
        "transvestic disorder": {"transvestic", "disorder"},
        "other specified paraphilic disorder": {"other", "specified", "paraphilic", "disorder"},
        "unspecified paraphilic disorder": {"unspecified", "paraphilic", "disorder"},

        # Other Mental Disorders and Additional Codes:
        "other specified mental disorder": {"other", "specified", "mental", "disorder"},
        "unspecified mental disorder": {"unspecified", "mental", "disorder"},
        "no diagnosis or condition": {"no", "diagnosis", "condition"},

        # Medication-Induced Movement Disorders and Other Adverse Effects of Medication:
        "neuroleptic malignant syndrome (NMS)": {"neuroleptic", "malignant", "syndrome", "nms"},
        "medication-induced parkinsonism": {"medication-induced", "parkinsonism"},
        "medication-induced acute dystonia": {"medication-induced", "acute", "dystonia"},
        "medication-induced acute akathisia": {"medication-induced", "acute", "akathisia"},
        "tardive dyskinesia": {"tardive", "dyskinesia"},
        "tardive dystonia": {"tardive", "dystonia"},
        "tardive akathisia": {"tardive", "akathisia"},
        "medication-induced postural tremor": {"medication-induced", "postural", "tremor"},
        "other medication-induced movement disorders": {"other", "medication-induced", "movement", "disorders"},
        "antidepressant discontinuation syndrome": {"antidepressant", "discontinuation", "syndrome"}

    }


    disorder_descriptions = {
        # Neurodevelopmental disorders:
        "intellectual developmental disorder (intellectual disability)": "Defined by deficits in both intellectual functions (like reasoning, problem-solving) and adaptive functioning (like communication, independent living), with onset during the developmental period",
        "global developmental delay": "Reserved for individuals under the age of 5 years when clinical severity cannot be reliably assessed. It is diagnosed when a child fails to meet expected developmental milestones in several areas of intellectual functioning.",
        "unspecified intellectual disability (intellectual developmental disorder)": "Used when the diagnosis of intellectual disability is presumed, but the individual is over the age of 5 years and it is difficult to assess the severity of the disability, possibly due to associated sensory or physical impairments.",
        "langauge disorder": "Characterized by persistent difficulties in the acquisition and use of language across modalities due to deficits in comprehension or production, impacting communication, social participation, academic achievement, or occupational performance.",
        "speech sound disorder": "Persistent difficulty with speech sound production that interferes with speech intelligibility or prevents verbal communication of messages.",
        "childhood-onset fluency disorder (stuttering)": "Characterized by disturbances in the normal fluency and time patterning of speech, which are inappropriate for the individual’s age and language skills, persist over time, and cause anxiety about speaking.",
        "pragmatic (social) communication disorder": "Characterized by primary difficulty with pragmatics, or the social use of language and communication. Deficits lead to challenges in following social rules of communication, storytelling, or understanding language's contextual nuances.",
        "autism spectrum disorder": "A disorder characterized by persistent deficits in social communication and social interaction across multiple contexts, along with restricted, repetitive patterns of behavior, interests, or activities, with symptoms present in the early developmental period.",
        "attention-deficit/hyperactivity disorder (ADHD)": "A persistent pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development, with symptoms present before age 12 and in multiple settings.",
        "specific learning disorder": "Characterized by difficulties learning and using academic skills, with the presence of at least one symptom that has persisted for at least 6 months, despite interventions targeting those difficulties.",
        "developmental coordination disorder": "Characterized by marked impairment in the development of motor coordination, significantly interfering with daily living activities and academic achievement, not attributable to a medical condition or intellectual disability.",
        "sterotypic movement disorder": "Involves repetitive, seemingly driven, and purposeless motor behavior (e.g., hand flapping, body rocking) that interferes with social, academic, or other activities and may result in self-injury.",
        "tic disorder": "Includes conditions like Tourette's Disorder, characterized by multiple motor and one or more vocal tics present for more than one year, with onset before age 18.",

        # Anxiety Disorders:
        "social anxiety disorder": "Social Anxiety Disorder is defined as a marked or intense fear or anxiety of social situations in which the individual may be scrutinized by others. This anxiety can involve a fear of being judged as anxious, weak, or unlikable, and it typically leads to avoidance of social situations or enduring them with significant distress.",
        "separation anxiety disorder": "Characterized by excessive fear or anxiety concerning separation from home or attachment figures that is developmentally inappropriate. This includes distress when separation is anticipated, worry about losing major attachment figures, or reluctance to be alone.",
        "selective mutism": "A consistent failure to speak in specific social situations where there is an expectation for speaking (e.g., at school) despite speaking in other situations. This condition interferes with educational or occupational achievement and social communication.",
        "specific phobia": "Marked fear or anxiety about a specific object or situation (e.g., flying, heights, animals) that is out of proportion to the actual danger posed by the specific object or situation and typically lasts for six months or more.",
        "panic disorder": "Recurrent unexpected panic attacks, which are abrupt surges of intense fear or discomfort that reach a peak within minutes, accompanied by physical and cognitive symptoms such as palpitations, sweating, shaking, shortness of breath, feelings of unreality, or fear of dying.",
        "panic attack specifier": "Refers to the occurrence of a panic attack, which is defined by an abrupt surge of intense fear or discomfort that reaches a peak within minutes and includes at least four of the 13 symptoms such as heart palpitations, sweating, trembling, shortness of breath, and fear of losing control or dying.",
        "agoraphobia": "Marked fear or anxiety about two or more of the following five situations: using public transportation, being in open spaces, being in enclosed places, standing in line or being in a crowd, or being outside of the home alone. The individual avoids these situations because they believe escape might be difficult or help might not be available in the event of panic-like symptoms.",
        "generalized anxiety disorder": "Excessive anxiety and worry, occurring more days than not for at least six months, about a number of events or activities. The individual finds it difficult to control the worry, and the anxiety is associated with symptoms such as restlessness, fatigue, difficulty concentrating, irritability, muscle tension, and sleep disturbance.",
        "substance / medication induced anxiety disorder": "Anxiety or panic attacks that develop during or soon after substance intoxication or withdrawal, or after exposure to a medication, and are attributable to the physiological effects of the substance/medication.",
        "anxiety disorder due to another medical condition": "Clinically significant anxiety that is judged to be directly caused by another medical condition, as evidenced by history, physical examination, or laboratory findings.",
        "other specified anxiety disorder": "This category applies to presentations of anxiety symptoms that cause clinically significant distress or impairment but do not meet the full criteria for any of the other anxiety disorders. The clinician provides a specific reason why the presentation does not meet the criteria.",

        # Depressive Disorders:
        "chronic depressive disorder": "Chronic Depressive Disorder (CDD) is a persistent and long-term form of depression where symptoms are less severe but last for an extended period, often for years.",
        "disruptive mood dysfunction": "Defined by chronic, severe, and persistent irritability, with frequent temper outbursts that are disproportionate in intensity or duration to the situation. The irritability must be present most of the day, nearly every day, between outbursts.",
        "major depressive disorder": "Characterized by a persistent and pervasive depressed mood or loss of interest or pleasure in nearly all activities. This disorder includes other symptoms such as significant weight changes, sleep disturbances, fatigue, feelings of worthlessness or excessive guilt, difficulty concentrating, and recurrent thoughts of death or suicide ",
        "persistent depressive disorder (dysthymia)": "A chronic form of depression where a person experiences a depressed mood for most of the day, for more days than not, for at least two years (or one year for children and adolescents). Symptoms may include poor appetite, insomnia or hypersomnia, low energy or fatigue, low self-esteem, poor concentration, and feelings of hopelessness.",
        "premenstrual dysphoric disorder": "This disorder is marked by mood lability, irritability, dysphoria, and anxiety that occur repeatedly during the premenstrual phase of the menstrual cycle and remit around the onset of menses or shortly thereafter. These mood symptoms must significantly interfere with work, school, or usual social activities and relationships.",
        "substance/medication-induced depressive disorder": "A depressive disorder caused by the use of or withdrawal from a substance or medication. The symptoms are characterized by a prominent and persistent disturbance in mood, primarily involving depressed mood or loss of interest or pleasure in almost all activities.",
        "depressive disorder due to another medical condition": "A depressive disorder that is directly attributable to the physiological effects of another medical condition. The mood disturbance may involve depressed mood or markedly diminished interest or pleasure in all, or almost all, activities.",
        "other specified depressive disorder": "This category is used when depressive symptoms cause significant distress or impairment but do not meet the full criteria for any other depressive disorder. The clinician specifies the reason that the presentation does not meet the criteria for another depressive disorder.",
        "unspecified depressive disorder": "Used when depressive symptoms cause significant distress or impairment but do not meet the criteria for any specific depressive disorder, and the clinician chooses not to specify the reason, or there is insufficient information to make a more specific diagnosis.",

        # Schizophrenia and other Psychotic Disorders
        "schizotypal (personality) disorder": "Characterized by pervasive patterns of social and interpersonal deficits, including discomfort with close relationships, as well as cognitive or perceptual distortions and eccentric behaviors. Individuals may exhibit odd beliefs, magical thinking, and social anxiety.",
        "delusional disorder": "Involves the presence of one or more delusions (false beliefs) that persist for at least one month. Apart from the delusions, the person's functioning is not markedly impaired, and behavior is not obviously bizarre or odd.",
        "brief psychotic disorder": "A short-term psychotic disorder lasting more than one day but less than one month, with a sudden onset of at least one of the following: delusions, hallucinations, disorganized speech, or grossly disorganized or catatonic behavior.",
        "schizophreniform": "Similar to schizophrenia, but with a shorter duration of symptoms, lasting at least one month but less than six months. It includes symptoms like delusions, hallucinations, disorganized speech, and negative symptoms (e.g., diminished emotional expression).",
        "schizophrenia": "A severe mental disorder characterized by a range of symptoms, including delusions, hallucinations, disorganized thinking, grossly disorganized or abnormal motor behavior (including catatonia), and negative symptoms. These symptoms must persist for at least six months.",
        "schizoaffective disorder": "Features a combination of schizophrenia symptoms (like delusions or hallucinations) and mood disorder symptoms (either depressive or manic episodes). The psychotic features must be present for a significant portion of the illness duration, even outside of mood episodes.",
        "substance/medication-induced psychotic disorder": "Psychotic symptoms, such as delusions or hallucinations, are caused by the use of or withdrawal from a substance or medication. The symptoms typically emerge during or shortly after substance use.",
        "psychotic disorder due to another medical condition": "Psychotic symptoms (delusions or hallucinations) are directly attributable to another medical condition. The diagnosis is confirmed through clinical assessment and testing.",
        "catatonia associated with another mental disorder (catatonia specifier)": "A syndrome of psychomotor disturbances associated with various mental disorders, including schizophrenia. Symptoms can include stupor, mutism, negativism, posturing, and rigidity.",
        "catatonic disorder due to another medical condition": "Catatonia that is directly attributable to a medical condition, as evidenced by clinical examination and diagnostic testing.",
        "other specified schizophrenia spectrum and other psychotic disorder": "This category is used when psychotic symptoms cause significant distress or impairment but do not meet the full criteria for any specific disorder in the schizophrenia spectrum. The clinician specifies the reason why the criteria are not fully met.",
        "unspecified schizophrenia spectrum and other psychotic disorder": "Used when psychotic symptoms cause significant distress or impairment, but there is insufficient information to make a more specific diagnosis, or the clinician chooses not to specify the reason.",
        "unspecified catatonia": "Used when the clinical presentation suggests the presence of catatonia, but there is insufficient information to determine the specific cause or associated condition.",

        # Bipolar Disorders and Related Disorders:
        "bipolar I(1) disorder": "Defined by the occurrence of at least one manic episode, which may be preceded by and possibly followed by hypomanic or major depressive episodes. A manic episode involves a distinct period of abnormally and persistently elevated, expansive, or irritable mood, and increased activity or energy.",
        "bipolar II(2) disorder": "Characterized by a pattern of depressive episodes and hypomanic episodes, but not the full-blown manic episodes that are typical of Bipolar I Disorder. The hypomanic episodes in Bipolar II Disorder do not cause the same level of impairment as the manic episodes in Bipolar I.",
        "cyclothymic disorder": "Involves numerous periods of hypomanic symptoms and periods of depressive symptoms that do not meet the criteria for a hypomanic episode or a major depressive episode. These symptoms occur for at least two years in adults (one year in children and adolescents) and are persistent, with symptom-free intervals lasting no longer than two months.",
        "substance / medication-induced bipolar and related disorder": "Involves a prominent and persistent disturbance in mood that is characterized by an abnormally elevated, expansive, or irritable mood, with or without depressed mood, and an abnormally increased activity or energy. This mood disturbance is due to the direct physiological effects of a substance or medication.",
        "bipolar and related disorder due to another medical condition": "This disorder involves a mood disturbance, characterized by abnormally elevated, expansive, or irritable mood, and increased activity or energy, that is directly attributable to another medical condition.",
        "other specified bipolar and related disorder": "This category is used for conditions in which symptoms characteristic of bipolar and related disorders cause significant distress or impairment in social, occupational, or other important areas of functioning but do not meet the full criteria for any specific bipolar disorder. The clinician provides the specific reason why the criteria are not met.",
        "unspecified bipolar and related disorder": "Used when the clinician chooses not to specify the reason that the criteria are not met for a specific bipolar disorder, or there is insufficient information to make a more specific diagnosis.",

        # obsessive-compulsive disorder (ocd):
        "obsessive - compulsive disorder (OCD)": "Characterized by the presence of obsessions (recurrent and persistent thoughts, urges, or images) and/or compulsions (repetitive behaviors or mental acts) that are time-consuming (taking more than one hour per day) or cause significant distress or impairment.",
        "body dysmorphic disorder": "Involves a preoccupation with one or more perceived defects or flaws in physical appearance that are not observable or appear slight to others. This preoccupation leads to repetitive behaviors (e.g., mirror checking, excessive grooming) or mental acts (e.g., comparing appearance with others).",
        "hoarding disorder": "Persistent difficulty discarding or parting with possessions, regardless of their actual value, due to a perceived need to save them and distress associated with discarding them. This behavior results in the accumulation of possessions that clutter living areas and substantially compromise their intended use.",
        "trichotillomania (hair - pulling disorder)": "Recurrent pulling out of one's hair, leading to hair loss, accompanied by repeated attempts to decrease or stop the behavior. The hair pulling causes clinically significant distress or impairment in functioning.",
        "excoriation (skin - picking) disorder": "Recurrent skin picking resulting in skin lesions, accompanied by repeated attempts to decrease or stop the behavior. The skin picking causes clinically significant distress or impairment in functioning.",
        "substance / medication - induced obsessive - compulsive and related disorder": "Obsessive-compulsive symptoms that are caused by the use of or withdrawal from a substance or medication. The symptoms are directly attributable to the substance or medication involved.",
        "obsessive - compulsive and related disorder due to another medical condition": "Obsessive-compulsive symptoms that are directly attributable to the physiological effects of another medical condition. This diagnosis is made based on clinical assessment and testing.",
        "other specified obsessive - compulsive and related disorder": "This category is used when symptoms characteristic of an obsessive-compulsive and related disorder cause significant distress or impairment in functioning but do not meet the full criteria for any specific disorder in this category. The clinician specifies the reason why the criteria are not fully met.",
        "unspecified obsessive - compulsive and related disorder": "Used when obsessive-compulsive symptoms cause significant distress or impairment but do not meet the criteria for any specific disorder in this category, and the clinician chooses not to specify the reason, or there is insufficient information to make a more specific diagnosis.",

        # Trauma and Stressor - related:
        "reactive attachment disorder": "Characterized by a pattern of markedly disturbed and developmentally inappropriate attachment behaviors in which a child rarely or minimally turns preferentially to an attachment figure for comfort, support, protection, and nurturance. This disorder is associated with social neglect or other situations that limit opportunities to form selective attachments.",
        "disinhibited social engagement disorder": "Involves a pattern of behavior in which a child actively approaches and interacts with unfamiliar adults and exhibits overly familiar verbal or physical behavior that violates social boundaries. This disorder often arises from social neglect or a lack of consistent caregiving",
        "posttraumatic stress disorder": "A condition triggered by exposure to a traumatic event, characterized by symptoms such as intrusive thoughts, flashbacks, avoidance of reminders of the trauma, negative changes in thoughts and mood, and heightened arousal and reactivity. PTSD symptoms must persist for more than one month and cause significant distress or impairment.",
        "acute stress disorder": "Similar to PTSD, this disorder occurs shortly after a traumatic event and includes symptoms like dissociation, intrusive memories, avoidance, and hyperarousal. The key difference is that symptoms last for a shorter period—between 3 days and 1 month after the trauma.",
        "adjustment disorder": "A condition where the grieving process is prolonged, lasting beyond the expected time frame, with intense yearning or longing for the deceased, preoccupation with the deceased, and significant disruption in personal, family, or occupational functioning.",
        "prolonged grief disorder": "A condition where the grieving process is prolonged, lasting beyond the expected time frame, with intense yearning or longing for the deceased, preoccupation with the deceased, and significant disruption in personal, family, or occupational functioning.",
        "other specific trauma- and stressor-related disorder": "Used when trauma-related symptoms cause significant distress or impairment but do not meet the full criteria for any specific trauma- or stressor-related disorder. The clinician specifies the reason why the criteria are not met.",
        "unspecified trauma- and stressor- related disorder": "This category is used when symptoms of a trauma- or stressor-related disorder cause significant distress or impairment, but there is insufficient information to specify the diagnosis or the clinician chooses not to specify the reason why the criteria are not met.",

        # dissociative disorders:
        "dissociative identity disorder": "Characterized by the presence of two or more distinct personality states or an experience of possession, with marked discontinuity in sense of self and sense of agency, accompanied by related alterations in affect, behavior, consciousness, memory, perception, cognition, and/or sensory-motor functioning. These symptoms may be observed by others or reported by the individual.",
        "dissociative amnesia": "Involves an inability to recall important autobiographical information, usually of a traumatic or stressful nature, that is inconsistent with ordinary forgetting. This can manifest as localized (failure to recall events during a specific period), selective (failure to recall some but not all events during a period), or generalized (complete loss of memory for one’s life history).",
        "depersonalization/derealization disorder": " Characterized by persistent or recurrent experiences of depersonalization (detachment or feeling of being an outside observer to one’s thoughts, feelings, body, or actions) and/or derealization (experiences of unreality or detachment with respect to surroundings). During these experiences, reality testing remains intact.",
        "other specified dissociative disorder": "This category applies to presentations in which symptoms characteristic of a dissociative disorder cause clinically significant distress or impairment but do not meet the full criteria for any of the specific dissociative disorders. The specific reason for the presentation not meeting the full criteria is communicated, such as 'dissociative trance''.",
        "unspecified dissociative disorder": "Used when symptoms characteristic of a dissociative disorder cause significant distress or impairment but do not meet the full criteria for any specific dissociative disorder. This category is used when the clinician chooses not to specify the reason the criteria are not met or when there is insufficient information to make a more specific diagnosis.",
        # somatic symptom and related disorders:
        "somatic symptom disorder": "Somatic symptom disorder is characterized by somatic symptoms that are distressing or result in significant disruption of daily life, accompanied by excessive thoughts, feelings, or behaviors related to these symptoms or associated health concerns as manifested by at least one of the following:\nDisproportionate and persistent thoughts about the seriousness of one's symptoms.\nPersistently high level of anxiety about health or symptoms.\nExcessive time and energy devoted to these symptoms or health concerns.",
        "illness (anxiety) disorder": "Illness anxiety disorder is preoccupation with having or acquiring a serious illness. Somatic symptoms are not present, or if present, are only mild in intensity. If another medical condition is present or there is a high risk for developing a medical condition, the preoccupation is clearly excessive or disproportionate.",
        "conversion disorder (functional neurological symptom disorder)": "Conversion disorder (functional neurological symptom disorder) is characterized by one or more symptoms of altered voluntary motor or sensory function. Clinical findings provide evidence of incompatibility between the symptom and recognized neurological or medical conditions.",
        "(somatic) psychological factors affecting other medical condtions ": "Psychological factors affecting other medical conditions is characterized by the presence of one or more clinically significant psychological or behavioral factors that adversely affect a medical condition by increasing the risk for suffering, death, or disability.",
        "factitious disorder": "Factitious disorder involves the falsification of medical or psychological signs and symptoms in oneself or others that are associated with the identified deception. The individual presents themselves to others as ill, impaired, or injured.",
        "other specified somatic symptoms and related disorder": "This category applies to presentations in which symptoms characteristic of a somatic symptom and related disorder that cause clinically significant distress or impairment in social, occupational, or other important areas of functioning predominate but do not meet the full criteria for any of the disorders in the somatic symptom and related disorders diagnostic class.",
        "unspecified somatic symptoms and related disorder": "This category applies to presentations in which symptoms characteristic of a somatic symptom and related disorder that cause clinically significant distress or impairment in social, occupational, or other important areas of functioning predominate but do not meet the full criteria for any of the disorders in the somatic symptom and related disorders diagnostic class. The 'unspecified somatic symptom and related disorder' category is used when the clinician chooses not to specify the reason that the criteria are not met for a specific somatic symptom and related disorder, or there is insufficient information to make a more specific diagnosis.",

        # feeding and eating disorders:
        "pica": "The essential feature of pica is the eating of one or more nonnutritive, nonfood substances on a persistent basis over a period of at least 1 month, that is severe enough to warrant clinical attention.",
        "rumination disorder": "The essential feature of rumination disorder is the repeated regurgitation of food occurring after feeding or eating over a period of at least 1 month. The food may be re-chewed, re-swallowed, or spit out.",
        "avoidant/restrictive food intake disorder": "Avoidant/restrictive food intake disorder is characterized by avoidance or restriction of food intake that is associated with one (or more) of the following consequences:\n1.Significant weight loss (or failure to achieve expected weight gain or faltering growth in children).\n2.Significant nutritional deficiency.\n3.Dependence on enteral feeding or oral nutritional supplements.\n4.Marked interference with psychosocial functioning.",
        "anorexia nervosa": "Anorexia nervosa is characterized by persistent energy intake restriction; intense fear of gaining weight or of becoming fat, or persistent behavior that interferes with weight gain; and a disturbance in self-perceived weight or shape.",
        "bulimia nervosa": "Bulimia nervosa is defined by recurrent episodes of binge eating characterized by both of the following:\n1.Eating, in a discrete period of time, an amount of food that is definitely larger than what most individuals would eat in a similar period under similar circumstances.\n2.A sense of lack of control over eating during the episode (e.g., a feeling that one cannot stop eating or control what or how much one is eating).",
        "binge-eating disorder": "Binge-eating disorder is characterized by recurrent episodes of binge eating. An episode of binge eating is characterized by both of the following:\n1.Eating, in a discrete period of time, an amount of food that is definitely larger than what most people would eat in a similar period under similar circumstances.\n2.A sense of lack of control over eating during the episode.",
        "other specified feeding or eating disorder": "This category applies to presentations in which symptoms characteristic of a feeding and eating disorder that cause clinically significant distress or impairment in social, occupational, or other important areas of functioning predominate but do not meet the full criteria for any of the disorders in the feeding and eating disorders diagnostic class. The 'other specified feeding or eating disorder' category is used in situations where the clinician chooses to communicate the specific reason that the presentation does not meet the criteria for any specific feeding and eating disorder.",
        "unspecified feeding or eating disorder": "This category applies to presentations in which symptoms characteristic of a feeding and eating disorder that cause clinically significant distress or impairment in social, occupational, or other important areas of functioning predominate but do not meet the full criteria for any of the disorders in the feeding and eating disorders diagnostic class. The 'unspecified feeding or eating disorder' category is used when the clinician chooses not to specify the reason that the criteria are not met for a specific feeding and eating disorder, or there is insufficient information to make a more specific diagnosis.",

        # elimination disorders:
        "enuresis": "This involves repeated voiding of urine into inappropriate places (e.g., bed or clothes). It can be classified based on the time of occurrence:\nNocturnal only (during sleep)\nDiurnal only (during waking hours)\nNocturnal and diurnal",
        "encopresis": "This involves the repeated passage of feces into inappropriate places (e.g., clothing or floor). It is specified by:\nWith constipation and overflow incontinence\nWithout constipation and overflow incontinence",
        "other specified elimination disorder": "This category is used when symptoms cause significant distress or impairment but do not meet the full criteria for any specific elimination disorder. The specific reason for not meeting the criteria is usually documented (e.g., low-frequency enuresis).",
        "unspecified elimination disorder": "This is used when symptoms characteristic of an elimination disorder are present, causing significant distress or impairment, but there is insufficient information to make a more specific diagnosis (e.g., in emergency room settings).",

        # sleep - wake disorders (page 407-page 477):
        "insomnia disorder": "Dissatisfaction with sleep quantity or quality, associated with one (or more) of the following symptoms: difficulty initiating sleep; difficulty maintaining sleep; early-morning awakening with inability to return to sleep",
        "hypersomnolence disorder": "Self-reported excessive sleepiness (hypersomnolence) despite a main sleep period lasting at least 7 hours, with at least one of the following symptoms: recurrent periods of sleep or lapses into sleep within the same day; a prolonged main sleep episode of more than 9 hours per day that is nonrestorative; difficulty being fully awake after abrupt awakening",
        "narcolepsy": "Recurrent periods of an irrepressible need to sleep, lapsing into sleep, or napping occurring within the same day",
        "obstructive sleep apnea hypopnea": "Repeated episodes of upper (pharyngeal) airway obstruction (apneas and hypopneas) during sleep",
        "central sleep apnea": "Repetitive episodes of apneas and hypopneas during sleep caused by variability in respiratory effort",
        "sleep-related hypoventilation": "Episodes of decreased respiration associated with elevated CO2 levels that occur during sleep",
        "circadian rhythm sleep-wake disorder": "Persistent or recurrent pattern of sleep disruption that is primarily due to an alteration of the circadian system or to a misalignment between the endogenous circadian rhythm and the sleep-wake schedule required by an individual's physical environment or social or professional schedule",
        "non-rapid eye movement (non-REM) sleep arousal": "Recurrent episodes of incomplete awakening from sleep, usually occurring during the first third of the major sleep episode, accompanied by either sleepwalking or sleep terrors",
        "nightmare disorder": "Repeated occurrences of extended, extremely dysphoric, and well-remembered dreams that usually involve efforts to avoid threats to survival, security, or physical integrity",
        "rapid eye movement (REM) sleep behavior disorder": "Repeated episodes of arousal during sleep associated with vocalization and/or complex motor behaviors",
        "restless legs syndrome": "An urge to move the legs, usually accompanied by or in response to uncomfortable and unpleasant sensations in the legs",
        "substance/medication-induced sleep disorder": "A prominent sleep disturbance that is sufficiently severe to warrant independent clinical attention",
        "other specified sleep-wake disorder": "Symptoms characteristic of a sleep-wake disorder that cause clinically significant distress or impairment in social, occupational, or other important areas of functioning but do not meet the full criteria for any of the disorders in the sleep-wake disorders diagnostic class",
        "unspecified sleep-wake disorder": "Symptoms characteristic of a sleep-wake disorder that cause clinically significant distress or impairment in social, occupational, or other important areas of functioning but do not meet the full criteria for any of the disorders in the sleep-wake disorders diagnostic class",

        # sexual dysfunctions (page 477- page 511):
        "delayed ejaculation": "Difficulty in or inability to achieve ejaculation during partnered sexual activity.",
        "erectile disorder": "Difficulty in obtaining or maintaining an erection during sexual activity or marked decrease in erectile rigidity.",
        "female orgasmic disorder": "Delay in, infrequency of, or absence of orgasm or reduced intensity of orgasmic sensations.",
        "female sexual interest/arousal disorder": "Lack of or significantly reduced sexual interest/arousal as manifested by at least three of several possible symptoms (e.g., absent/reduced interest in sexual activity, absent/reduced sexual/erotic thoughts or fantasies).",
        "genito-pelvic pain/penetration disorder": "Difficulties with vaginal penetration, vulvovaginal or pelvic pain during intercourse, fear or anxiety about pain in anticipation of, during, or as a result of vaginal penetration, or tensing or tightening of the pelvic floor muscles during attempted vaginal penetration.",
        "male hypoactive sexual desire disorder": "Persistently or recurrently deficient (or absent) sexual/erotic thoughts or fantasies and desire for sexual activity.",
        "premature (early) ejaculation": "A pattern of ejaculation occurring during partnered sexual activity within approximately 1 minute following vaginal penetration and before the individual wishes it.",
        "substance/medication-induced sexual disorder": "Sexual dysfunctions associated with substance use, including alcohol, opioids, sedatives, hypnotics, anxiolytics, stimulants, and other substances.",
        "other specified sexual dysfunction": "Symptoms characteristic of a sexual dysfunction that cause clinically significant distress but do not meet the full criteria for any of the disorders in the sexual dysfunctions diagnostic class.",
        "unspecified sexual dysfunctional": "Symptoms characteristic of a sexual dysfunction that cause clinically significant distress but do not meet the full criteria for any of the disorders in the sexual dysfunctions diagnostic class",

        # gender dysphoria (page 511- page 521):
        "gender dysphoria in children": "A marked incongruence between one’s experienced/expressed gender and assigned gender, lasting at least 6 months, and manifested by a strong desire to be of the other gender or insistence that one is the other gender, along with other criteria.",
        "gender dysphoria in adolescents and adults": "A marked incongruence between one’s experienced/expressed gender and assigned gender, lasting at least 6 months, with at least two of several possible criteria (e.g., a strong desire to be rid of one’s primary and/or secondary sex characteristics).",
        "other specified gender dysphoria": "This category applies to presentations where symptoms characteristic of gender dysphoria cause clinically significant distress or impairment but do not meet the full criteria for gender dysphoria. The specific reason for not meeting the criteria is usually documented.",
        "unspecified gender dysphoria": "This category is used when symptoms characteristic of gender dysphoria cause clinically significant distress or impairment but do not meet the full criteria for gender dysphoria, and there is insufficient information to make a more specific diagnosis.",

        # disruptive, impulse-control, and conduct disorders (page 521- page 543):
        "oppositional defiant disorder": "A pattern of angry/irritable mood, argumentative/defiant behavior, or vindictiveness lasting at least 6 months.",
        "intermittent explosive disorder": "Recurrent behavioral outbursts representing a failure to control aggressive impulses as manifested by verbal or physical aggression.",
        "conduct disorder": "A repetitive and persistent pattern of behavior in which the basic rights of others or major age-appropriate societal norms or rules are violated.",
        ##"antisocial personality disorder":"A pervasive pattern of disregard for and violation of the rights of others, occurring since age 15 years.",
        "pyromania": " Deliberate and purposeful fire setting on more than one occasion.",
        "kleptomania": "Recurrent failure to resist impulses to steal objects that are not needed for personal use or for their monetary value.",
        "other specified disruptive, impulse-control, and conduct disorder": "Symptoms characteristic of a disruptive, impulse-control, and conduct disorder that cause significant distress or impairment but do not meet the full criteria for any of the disorders in this diagnostic class.",
        "unspecified disruptive, impulse-control, and conduct disorder": "Symptoms characteristic of a disruptive, impulse-control, and conduct disorder that cause significant distress or impairment but do not meet the full criteria for any of the disorders in this diagnostic class, with the specific reason not specified.",

        # substance-related and addicted disorders(page 543 - page 667):
        "alcohol-related disorders": "Includes Alcohol Use Disorder, Alcohol Intoxication, Alcohol Withdrawal, and other alcohol-induced disorders.",
        "caffeine-related disorders": "Includes Caffeine Intoxication, Caffeine Withdrawal, and other caffeine-induced disorders.",
        "cannabis-related disorders": "Includes Cannabis Use Disorder, Cannabis Intoxication, Cannabis Withdrawal, and other cannabis-induced disorders.",
        "hallucinogen-related disorders": "Use Disorder, Other Hallucinogen Use Disorder, Hallucinogen Persisting Perception Disorder, and other hallucinogen-induced disorders.",
        "inhalant-related disorders": " Includes Inhalant Use Disorder and other inhalant-induced disorders.",
        "opioid-related disorders": "Includes Opioid Use Disorder, Opioid Intoxication, Opioid Withdrawal, and other opioid-induced disorders.",
        "sedative-related,hypnotic-related,or anxiolytic-related disorders": " Includes Sedative-, Hypnotic-, or Anxiolytic Use Disorder, Intoxication, Withdrawal, and other related induced disorders.",
        "stimulant-related disorders": "Includes Amphetamine-Type Substance, Cocaine, or Other Stimulant Use Disorder, Stimulant Intoxication, Stimulant Withdrawal, and other stimulant-induced disorders.",
        "tobacco-related disorders": "Includes Tobacco Use Disorder, Tobacco Withdrawal, and other tobacco-induced disorders.",
        "other (or unknown) substance-related disorders": "Includes disorders related to the use of other or unknown substances not classified under the previous categories.",

        "alcohol use disorder": "A problematic pattern of alcohol use leading to clinically significant impairment or distress, as manifested by at least two of several specified criteria, occurring within a 12-month period.",
        "alcohol intoxication": "Recent ingestion of alcohol leading to significant problematic behavioral or psychological changes, with signs or symptoms such as slurred speech, incoordination, or impaired attention.",
        "alcohol withdrawal": "Cessation or reduction in heavy and prolonged alcohol use, leading to specific symptoms such as autonomic hyperactivity, hand tremor, insomnia, or nausea.",
        "caffeine intoxication": "Recent consumption of caffeine, usually in excess of 250 mg (more than 2-3 cups of brewed coffee), leading to five or more specific symptoms:\n1.Restlessness\n2.Nervousness\n3.Excitement\n4.Insomnia\n5.Flushed face\n6.Diuresis (increased urination\n6.Gastrointestinal disturbance\n7.Muscle twitching\n8.Rambling flow of thought and speech\n9.Tachycardia (increased heart rate) or cardiac arrhythmia\n10.Periods of inexhaustibility (not feeling tired)\n11.Psychomotor agitation",
        "caffeine withdrawal": "Prolonged daily use of caffeine followed by abrupt cessation or reduction, leading to symptoms like headache, fatigue, or dysphoric mood.",
        "cannabis use disorder": "A problematic pattern of cannabis use leading to clinically significant impairment or distress, as manifested by at least two of several criteria, occurring within a 12-month period.",
        "cannabis intoxication": "Recent use of cannabis leading to clinically significant problematic behavioral or psychological changes, with symptoms such as conjunctival injection, increased appetite, or dry mouth.",
        "cannabis withdrawal": "Cessation of cannabis use that has been heavy and prolonged, leading to three or more specific symptoms, such as irritability, sleep difficulty, or decreased appetite.",
        "phencyclidine (PCP) use disorder": "A problematic pattern of phencyclidine use leading to clinically significant impairment or distress.",
        "other hallucinogen use disorder": "A problematic pattern of hallucinogen use other than phencyclidine, leading to clinically significant impairment or distress.",
        "inhalant use disorder": "A problematic pattern of inhalant use leading to clinically significant impairment or distress.",
        "opioid use disorder": "A problematic pattern of opioid use leading to clinically significant impairment or distress.",
        "opioid intoxication": "Recent use of an opioid leading to problematic behavioral or psychological changes, with specific symptoms such as pupillary constriction or drowsiness.",
        "opioid withdrawal": "Cessation of opioid use that has been heavy and prolonged, or administration of an opioid antagonist, leading to specific symptoms such as dysphoric mood, nausea, or muscle aches.",
        "sedative, hyponotic, or anxiolytic use disorder": "A problematic pattern of sedative, hypnotic, or anxiolytic use leading to clinically significant impairment or distress.",
        "stimulant use disorder": "A problematic pattern of stimulant use leading to clinically significant impairment or distress.",
        "tobacco use disorder": "A problematic pattern of tobacco use leading to clinically significant impairment or distress.",
        "gambling disorder": "Persistent and recurrent problematic gambling behavior leading to clinically significant impairment or distress, as indicated by the individual exhibiting four or more of several specified criteria in a 12-month period.",

        # neurocognitive disorders (page 667- page 733):
        "delirium": " Characterized by a disturbance in attention and awareness that develops over a short period, represents a change from baseline attention and awareness, and tends to fluctuate in severity during the course of the day.",
        "major neurocognitive disorder": "Significant cognitive decline from a previous level of performance in one or more cognitive domains (e.g., complex attention, executive function, learning, and memory) that interferes with independence in everyday activities.",
        "mild neurocognitive disorder": "Modest cognitive decline from a previous level of performance in one or more cognitive domains that does not interfere with capacity for independence in everyday activities but may require greater effort or compensatory strategies.",
        "major or mild neurocognitive disorder due to alzheimer's disease": " A diagnosis given when the criteria for major or mild neurocognitive disorder are met, with gradual onset and progressive cognitive decline, and Alzheimer's disease is either the probable or possible cause.",
        "major or mild frontotemporal neurocognitive disorder": "Cognitive decline is associated with frontotemporal lobar degeneration, often presenting with either behavioral variant or language variant.",
        "major or mild neurocognitive disorder with lewy bodies": "Progressive cognitive decline associated with visual hallucinations, parkinsonism, and fluctuating cognition.",
        "major or mild vascular neurocognitive disorder": "Cognitive decline resulting from cerebrovascular events, presenting with a stepwise progression of cognitive deficits, often after a stroke.",
        "major or mild neurocognitive disorder due to traumatic brain injury": " Cognitive decline following a traumatic brain injury, with onset of the neurocognitive disorder immediately after the occurrence of the injury or after regaining consciousness.",
        "substance/medication-induced major or mild neurocognitive disorder": " Cognitive decline related to the persistent effects of substance use or exposure to toxins.",
        "major or mild neurocognitive disorder due to HIV injection": "Cognitive decline associated with HIV infection, not better explained by non-HIV conditions.",
        "major or mild neurocognitive disorder due to prion diseases": "Rapidly progressing cognitive decline caused by prion disease, such as Creutzfeldt-Jakob disease.",
        "major or mild neurocognitive disorder due to parkinson's disease": "Cognitive decline that occurs in the context of Parkinson’s disease, often with a decline in executive function, attention, and memory.",
        "major or mild neurocognitive disorder due to huntington's disease": "Cognitive decline associated with Huntington’s disease, typically with early changes in executive function.",
        "major or mild neurocognitive disorder due to another medical condition": "Cognitive decline caused by a medical condition not listed elsewhere.",
        "major or mild neurocognitive disorder due to multiple etiologies": "Cognitive decline resulting from more than one cause, such as Alzheimer’s disease and cerebrovascular disease.",
        "unspecified neurocognitive disorder": "Used when symptoms of cognitive decline are present, but there is insufficient information to determine the specific cause.",

        "alzheimer's disease": "A progressive neurodegenerative disease that primarily affects memory, thinking, and behavior. It is characterized by the gradual onset of cognitive impairment that worsens over time, eventually interfering with daily functioning. The pathology involves amyloid plaques and neurofibrillary tangles in the brain.",
        "frontotemporal degeneration": "A group of disorders caused by progressive cell degeneration in the brain's frontal or temporal lobes. It often results in significant changes in personality, behavior, or language. Unlike Alzheimer’s, it typically affects younger adults and may present with either behavioral changes or language difficulties.",
        "lewy body disease": "A neurodegenerative disorder characterized by the presence of Lewy bodies (abnormal aggregates of protein) in brain cells. It leads to cognitive decline, visual hallucinations, fluctuating levels of consciousness, and Parkinsonism (motor symptoms similar to Parkinson's disease).",
        "vascular disease": "Refers to cognitive impairment caused by conditions that block or reduce blood flow to the brain, depriving brain cells of vital oxygen and nutrients. This can result from strokes, transient ischemic attacks, or other conditions affecting the blood vessels in the brain.",
        "traumatic brain injury (TBI)": "An injury to the brain caused by an external force, such as a blow to the head. TBI can result in a range of cognitive impairments, including difficulties with attention, memory, and executive functioning. The severity and duration of cognitive symptoms can vary widely based on the extent of the injury.",
        "substance/medication use": "Cognitive impairment resulting from the chronic use of substances, including drugs and alcohol, or the use of medications. The effects can persist beyond the period of intoxication or withdrawal, and may include memory loss, difficulty concentrating, and impaired judgment.",
        "HIV infection": "HIV can affect the brain and lead to cognitive impairment. This occurs when the virus invades the central nervous system, causing a decline in cognitive functions such as memory, attention, and executive function, often referred to as HIV-associated neurocognitive disorder (HAND).",
        "prion disease": "A group of rare, fatal brain disorders caused by prions, which are misfolded proteins that cause other proteins in the brain to misfold as well. This leads to rapid cognitive decline and motor dysfunction. Creutzfeldt-Jakob disease is the most well-known prion disease.",
        "parkinson's disease": "A progressive neurological disorder that primarily affects movement, but can also lead to cognitive impairment. Symptoms include tremors, stiffness, slowness of movement, and balance problems. Cognitive decline can occur as the disease progresses, particularly affecting executive functions and memory.",
        "huntington's disease": "A hereditary neurodegenerative disorder caused by a genetic mutation. It leads to the progressive breakdown of nerve cells in the brain, affecting movement, cognition, and emotions. Cognitive symptoms often include difficulties with planning, organization, and memory.",
        "multiple etiologies": "Refers to cognitive impairment caused by more than one contributing factor or condition. For example, a person may have cognitive decline due to both Alzheimer's disease and cerebrovascular disease.",
        "unspecified etiology": "Used when cognitive impairment is observed, but the exact cause cannot be determined. This diagnosis is often provisional, pending further evaluation or testing.",

        # personality disorders (page 733- page 779):
        "cluster A personality disorders": "odd or eccentric behavior (paranoid personality disorder; schizoid personality disorder; schizotypal personality disorder)",
        "cluster B personality disorders": "dramatic, emotional, or erratic behavior (e.g., antisocial personality disorder; borderline personality disorder; histrionic personality disorder; narcissistic personality disorder",
        "cluster C personality disorder": "anxious or fearful behavior (e.g., avoidant personality disorder; dependent personality disorder; obsessive-compulsive personality disorder)",
        # cluster A personality disorders:
        "paranoid personality disorder": "A pattern of distrust and suspiciousness such that others' motives are interpreted as malevolent.",
        "schizoid personality disorder": "A pattern of detachment from social relationships and a restricted range of emotional expression.",
        "schizotypal personality disorder": "A pattern of acute discomfort in close relationships, cognitive or perceptual distortions, and eccentricities of behavior.",
        # cluster B personality disorders:
        "antisocial personality disorder": "A pattern of disregard for, and violation of, the rights of others.",
        "borderline personality disorder": "A pattern of instability in interpersonal relationships, self-image, and affects, and marked impulsivity.",
        "histrionic personality disorder": "A pattern of excessive emotionality and attention seeking.",
        "narcissistic personality disorder": "A pattern of grandiosity, need for admiration, and lack of empathy.",
        # cluster C personality disorders:
        "avoidant personality disorder": "A pattern of social inhibition, feelings of inadequacy, and hypersensitivity to negative evaluation.",
        "dependent personality disorder": "A pattern of submissive and clinging behavior related to an excessive need to be taken care of.",
        "obsessive-compulsive personality disorder": "A pattern of preoccupation with orderliness, perfectionism, and control.",
        # other personality disorders:
        "personality change due to another medical condition": "A personality disturbance that is a direct pathophysiological consequence of another medical condition.",
        "other specified personality disorder": "Presentations where symptoms characteristic of a personality disorder cause significant distress or impairment but do not meet the full criteria for any specific personality disorder.",
        "unspecified personality disorder": "Symptoms characteristic of a personality disorder that cause clinically significant distress or impairment but do not meet the full criteria for any specific personality disorder.",

        # paraphilic disorders (page 779- page 803):
        "voyeuristic disroder": "Over a period of at least 6 months, recurrent and intense sexual arousal from observing an unsuspecting person who is naked, in the process of disrobing, or engaging in sexual activity, as manifested by fantasies, urges, or behaviors.",
        "exhibitionist disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from the exposure of one’s genitals to an unsuspecting person, as manifested by fantasies, urges, or behaviors.",
        "frotteuristic disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from touching or rubbing against a nonconsenting person, as manifested by fantasies, urges, or behaviors.",
        "sexual masochism disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from the act of being humiliated, beaten, bound, or otherwise made to suffer, as manifested by fantasies, urges, or behaviors.",
        "sexual sadism disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from the physical or psychological suffering of another person, as manifested by fantasies, urges, or behaviors.",
        "pedophilic disorder": "Over a period of at least 6 months, recurrent, intense sexually arousing fantasies, sexual urges, or behaviors involving sexual activity with a prepubescent child or children (generally age 13 years or younger).",
        "fetishistic disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from either the use of nonliving objects or a highly specific focus on nongenital body part(s), as manifested by fantasies, urges, or behaviors.",
        "transvestic disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from cross-dressing, as manifested by fantasies, urges, or behaviors.",
        "other specified paraphilic disorder": "Presentations that cause clinically significant distress or impairment in social, occupational, or other important areas of functioning but do not meet the full criteria for any of the disorders in the paraphilic disorders diagnostic class.",
        "unspecified paraphilic disorder": "Symptoms characteristic of a paraphilic disorder that cause clinically significant distress or impairment in social, occupational, or other important areas of functioning but do not meet the full criteria for any specific paraphilic disorder.",

        # other mental disorders and additional codes (page 803 - page 807):
        "other specified mental disorder": "This category applies to presentations where symptoms characteristic of a mental disorder cause clinically significant distress or impairment but do not meet the full criteria for any specific mental disorder. The specific reason why the full criteria are not met is specified.",
        "unspecified mental disorder": "Used when symptoms characteristic of a mental disorder are present but there is insufficient information to determine the specific disorder, often used in situations where a more specific diagnosis cannot be made.",
        "no diagnosis or condition": "This code applies when an individual has been evaluated, and it is determined that no mental disorder or condition is present.",

        # medication-induced movement disorders and other adverse effects of medication (page 807 - page 821):
        "neuroleptic malignant syndrome (NMS)": "A life-threatening condition associated with the use of antipsychotic medications and other dopamine receptor-blocking agents. It is characterized by muscle rigidity, fever, autonomic instability, and altered mental status.",
        "medication-induced parkinsonism": "A disorder that mimics Parkinson’s disease, caused by medications, particularly antipsychotics and other dopamine receptor-blocking agents. Symptoms include tremors, bradykinesia (slowness of movement), rigidity, and postural instability.",
        "medication-induced acute dystonia": "A condition involving involuntary muscle contractions that can cause twisting and repetitive movements or abnormal postures. These symptoms can occur shortly after starting a medication.",
        "medication-induced acute akathisia": "A syndrome characterized by a subjective feeling of inner restlessness and a compelling need to be in constant motion. Patients may exhibit repetitive movements such as pacing or fidgeting.",
        "tardive dyskinesia": "A disorder characterized by repetitive, involuntary movements, particularly of the face and tongue, but also involving the limbs and trunk. It is a potential long-term side effect of antipsychotic medications.",
        "tardive dystonia": "A form of tardive dyskinesia where sustained muscle contractions cause twisting and repetitive movements or abnormal postures.",
        "tardive akathisia": "A variant of tardive dyskinesia that involves persistent, involuntary movements and restlessness that develops after long-term use of antipsychotic medications.",
        "medication-induced postural tremor": "A fine tremor occurring when the affected body part is held against gravity, such as holding out the arms. It can be caused by medications like lithium, valproate, and others.",
        "other medication-induced movement disorders": "This category includes movement disorders induced by medications that do not fit into the specific categories listed above. Examples might include movement disorders resembling neuroleptic malignant syndrome but caused by medications other than antipsychotics.",
        "antidepressant discontinuation syndrome": "A syndrome that can occur following the discontinuation or significant reduction in dosage of an antidepressant, particularly if the medication has been taken for an extended period. Symptoms can include flu-like symptoms, insomnia, nausea, imbalance, sensory disturbances, and hyperarousal.",

    }

    # Prioritize specific matching
    for disorder, keywords in disorder_keywords.items():
        if all(token in tokens for token in keywords):
            if disorder in disorder_descriptions:
                return disorder_descriptions[disorder]
            else:
                return "Sorry, I don't have information on that disorder right now."

    # If no exact matches, look for partial matches
    for disorder, keywords in disorder_keywords.items():
        if any(token in tokens for token in keywords):
            if disorder in disorder_descriptions:
                return disorder_descriptions[disorder]
            else:
                return "Sorry, I don't have information on that disorder right now."

    # If no matches are found, ask for clarification
    return "I'm not sure how to respond to that. Could you provide more details?"

# Main Program:
while True:
    user_input = input("You: ")

    #Exit condition:
    if user_input.lower() in {"exit", "quit", "bye", "see you","I am done","goodbye"}:
        print("EVE: Goodbye! Have a great day!")
        break

    response = eve(user_input)
    print(f"EVE: {response}")