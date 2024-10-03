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
        return "Hello! I am EVE. Your personal assistant for your DSM-5-TR. I can only provide you abbreviated definitions of clinical psychological disorders,\n however, I include every definition within the DSM-5-TR, so your learning is endless. \n For example, you can type 'what is social anxiety?', 'what might be tardive dyskinesia?', or 'REM Sleep Disorder'. Also, you can say, please provide a list."

    # Define list of disorders
    disorder_list = {"can you provide me a list", "list", "list please", "what is the list of disorders", "what is the list", "can I get the list", "what list?", "Can I get the list please"}
    if any(token in tokens for token in disorder_list):
        return ("""
                1.)Neurodevelopmental Disorders: Intellectual Developmental Disorder (Intellectual Disability); Global Developmental Delay; Unspecified Intellectual Disability (Intellectual Developmental Disorder); Language Disorder; Speech Sound Disorder; Childhood-Onset Fluency Disorder (Stuttering); Pragmatic (Social) Communication Disorder; Autism Spectrum Disorder; 
                Attention-Deficit/Hyperactivity Disorder (ADHD); Specific Learning Disorder; Developmental Coordination Disorder; Stereotypic Movement Disorder; Tic Disorder\n\n
                2.)Anxiety Disorders: Social Anxiety Disorder; Separation Anxiety Disorder; Selective Mutism; Specific Phobia; Panic Disorder; Panic Attack Specifier; Agoraphobia; Generalized Anxiety Disorder; Substance/Medication-Induced Anxiety Disorder; Anxiety Disorder Due to Another Medical Condition; Other Specified Anxiety Disorder\n\n
                3.)Depressive Disorders: Chronic Depressive Disorder; Disruptive Mood Dysregulation Disorder; Major Depressive Disorder; Persistent Depressive Disorder (Dysthymia); Premenstrual Dysphoric Disorder; Substance/Medication-Induced Depressive Disorder; Depressive Disorder Due to Another Medical Condition; Other Specified Depressive Disorder; 
                Unspecified Depressive Disorder; Schizophrenia Spectrum and Other Psychotic Disorders: Schizotypal (Personality) Disorder; Delusional Disorder; Brief Psychotic Disorder; Schizophreniform Disorder; Schizophrenia; Schizoaffective Disorder; Substance/Medication-Induced Psychotic Disorder; Psychotic Disorder Due to Another Medical Condition; 
                Catatonia Associated with Another Mental Disorder (Catatonia Specifier); Catatonic Disorder Due to Another Medical Condition; Other Specified Schizophrenia Spectrum and Other Psychotic Disorder; Unspecified Schizophrenia Spectrum and Other Psychotic Disorder; Unspecified Catatonia\n\n
                4.)Bipolar and Related Disorders: Bipolar I Disorder; Bipolar II Disorder; Cyclothymic Disorder; Substance/Medication-Induced Bipolar and Related Disorder; Bipolar and Related Disorder Due to Another Medical Condition; Other Specified Bipolar and Related Disorder; Unspecified Bipolar and Related Disorder\n\n
                5.)Obsessive-Compulsive and Related Disorders: Obsessive-Compulsive Disorder (OCD); Body Dysmorphic Disorder; Hoarding Disorder; Trichotillomania (Hair-Pulling Disorder); Excoriation (Skin-Picking) Disorder; Substance/Medication-Induced Obsessive-Compulsive and Related Disorder; Obsessive-Compulsive and Related Disorder Due to Another Medical Condition; 
                Other Specified Obsessive-Compulsive and Related Disorder; Unspecified Obsessive-Compulsive and Related Disorder\n\n
                6.)Trauma- and Stressor-Related Disorders: Reactive Attachment Disorder; Disinhibited Social Engagement Disorder; Posttraumatic Stress Disorder (PTSD); Acute Stress Disorder; Adjustment Disorder; Prolonged Grief Disorder; Other Specified Trauma- and Stressor-Related Disorder; Unspecified Trauma- and Stressor-Related Disorder\n\n
                7.)Dissociative Disorders: Dissociative Identity Disorder; Dissociative Amnesia; Depersonalization/Derealization Disorder; Other Specified Dissociative Disorder; Unspecified Dissociative; Disorder\n\n
                8.)Feeding and Eating Disorders: Pica; Rumination Disorder; Avoidant/Restrictive Food Intake Disorder; Anorexia Nervosa; Bulimia Nervosa; Binge-Eating Disorder; Other Specified Feeding or Eating Disorder; Unspecified Feeding or Eating Disorder\n\n
                9.)Elimination Disorders: Enuresis; Encopresis; Other Specified Elimination Disorder; Unspecified Elimination Disorder\n\n
                10.)Sleep-Wake Disorders: Insomnia Disorder; Hypersomnolence Disorder; Narcolepsy; Obstructive Sleep Apnea Hypopnea; Central Sleep Apnea; Sleep-Related Hypoventilation; Circadian Rhythm; Sleep-Wake Disorder; Non-Rapid Eye Movement (Non-REM) Sleep Arousal; Nightmare Disorder; Rapid Eye Movement (REM) Sleep Behavior Disorder; Restless Legs Syndrome; 
                Substance/Medication-Induced Sleep Disorder; Other Specified Sleep-Wake Disorder; Unspecified Sleep-Wake Disorder\n\n
                11.)Sexual Dysfunctions: Delayed Ejaculation; Erectile Disorder; Female Orgasmic Disorder; Female Sexual Interest/Arousal Disorder; Genito-Pelvic Pain/Penetration Disorder; Male Hypoactive Sexual Desire Disorder; Premature (Early) Ejaculation; Substance/Medication-Induced Sexual Disorder; Other Specified Sexual Dysfunction; Unspecified Sexual Dysfunction\n\n
                12.)Gender Dysphoria: Gender Dysphoria in Children; Gender Dysphoria in Adolescents and Adults; Other Specified Gender Dysphoria; Unspecified Gender Dysphoria\n\n
                13.)Disruptive, Impulse-Control, and Conduct Disorders: Oppositional Defiant Disorder; Intermittent Explosive Disorder; Conduct Disorder; Pyromania; Kleptomania; Other Specified Disruptive, Impulse-Control, and Conduct Disorder; Unspecified Disruptive, Impulse-Control, and Conduct Disorder\n\n
                14.)Substance-Related and Addictive Disorders: Alcohol-Related Disorders; Caffeine-Related Disorders; Cannabis-Related Disorders; Hallucinogen-Related Disorders; Inhalant-Related Disorders; Opioid-Related Disorders; Sedative-, Hypnotic-, or Anxiolytic-Related Disorders; Stimulant-Related Disorders; Tobacco-Related Disorders; 
                Other (or Unknown) Substance-Related Disorders; Alcohol Use Disorder; Alcohol Intoxication; Alcohol Withdrawal; Caffeine Intoxication; Caffeine Withdrawal; Cannabis Use Disorder; Cannabis Intoxication; Cannabis Withdrawal; Phencyclidine (PCP) Use Disorder; Other Hallucinogen Use Disorder; Inhalant Use Disorder; Opioid Use Disorder; 
                Opioid Intoxication; Opioid Withdrawal; Sedative, Hypnotic, or Anxiolytic Use Disorder; Stimulant Use Disorder; Tobacco Use Disorder; Gambling Disorder\n\n
                15.)Neurocognitive Disorders: Delirium; Major Neurocognitive Disorder; Mild Neurocognitive Disorder; Major or Mild Neurocognitive Disorder due to Alzheimer's Disease; Major or Mild; Frontotemporal Neurocognitive Disorder; Major or Mild Neurocognitive Disorder with Lewy Bodies; Major or Mild Vascular Neurocognitive Disorder; 
                Major or Mild Neurocognitive Disorder due to Traumatic Brain Injury; Substance/Medication-Induced Major or Mild Neurocognitive Disorder; Major or Mild Neurocognitive Disorder due to HIV Infection; Major or Mild Neurocognitive; Disorder due to Prion Disease; Major or Mild Neurocognitive Disorder due to Parkinson's Disease; 
                Major or Mild Neurocognitive Disorder due to Huntington's Disease; Major or Mild; Neurocognitive Disorder due to Another Medical Condition; Major or Mild Neurocognitive Disorder due to Multiple Etiologies; Unspecified Neurocognitive Disorder\n\n
                16.)Additional Neurocognitive Conditions: Alzheimer's Disease; Frontotemporal Degeneration; Lewy Body Disease; Vascular Disease; Traumatic Brain Injury (TBI); Substance/Medication Use; HIV Infection; Prion Disease; Parkinson's Disease; Huntington's Disease; Multiple Etiologies; Unspecified Etiology\n\n
                17.)Personality Disorders: Cluster A Personality Disorders; Paranoid Personality Disorder; Schizoid Personality Disorder; Schizotypal Personality Disorder; Cluster B Personality Disorders; Antisocial Personality Disorder; Borderline Personality Disorder; Histrionic Personality Disorder; 
                Narcissistic Personality Disorder; Cluster C Personality Disorders; Avoidant Personality Disorder; Dependent Personality Disorder; Obsessive-Compulsive Personality Disorder; Other Personality Disorders; Personality Change Due to Another Medical Condition; Other Specified Personality Disorder; Unspecified Personality Disorder\n\n
                18.)Paraphilic Disorders: Voyeuristic Disorder; Exhibitionist Disorder; Frotteuristic Disorder; Sexual Masochism Disorder; Sexual Sadism Disorder; Pedophilic Disorder; Fetishistic Disorder;Transvestic Disorder; Other Specified Paraphilic Disorder; Unspecified Paraphilic Disorder\n\n
                19.)Other Mental Disorders and Additional Codes: Other Specified Mental Disorder; Unspecified Mental Disorder; No Diagnosis or Condition; Medication-Induced Movement Disorders and Other Adverse Effects of Medication: Neuroleptic Malignant Syndrome (NMS); Medication-Induced Parkinsonism; Medication-Induced Acute Dystonia; 
                Medication-Induced Acute Akathisia; Tardive Dyskinesia; Tardive Dystonia; Tardive Akathisia; Medication-Induced Postural Tremor; Other Medication-Induced Movement Disorders; Antidepressant Discontinuation Syndrome"
                """)
    # Disorder keywords and descriptions
    disorder_keywords_maps= {
        # Neurodevelopmental disorders:
        "neurodevelopmental disorders":{"neurodevelopmental","disorders","neurodev"},
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
        "anxiety disorders":{"anxiety","disorders"},
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
        "schizophrenia and other Psychotic Disorder":{"schizophrenia","and","other","psychotic","disorder"},
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
        "bipolar disorders and related disorders": {"bipolar", "disorder", "related", "disorder"},
        "bipolar disorders": {"bipolar", "disorder"},
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
        "trauma and stressor-related disorders": {"trauma", "stressor", "related", "disorder"},
        "reactive attachment disorder": {"reactive", "attachment", "disorder"},
        "disinhibited social engagement disorder": {"disinhibited", "social", "engagement", "disorder"},
        "posttraumatic stress disorder (PTSD)": {"posttraumatic", "stress", "disorder", "ptsd"},
        "acute stress disorder": {"acute", "stress", "disorder"},
        "adjustment disorder": {"adjustment", "disorder"},
        "prolonged grief disorder": {"prolonged", "grief", "disorder"},
        "other specified trauma- and stressor-related disorder": {"other", "specified", "trauma", "stressor-related","disorder"},
        "unspecified trauma- and stressor-related disorder": {"unspecified", "trauma", "stressor-related", "disorder"},

        # Dissociative Disorders:
        "dissociated disorders": {"dissociated", "disorder"},
        "dissociative identity disorder": {"dissociative", "identity", "disorder"},
        "dissociative amnesia": {"dissociative", "amnesia"},
        "depersonalization/derealization disorder": {"depersonalization", "derealization", "disorder"},
        "other specified dissociative disorder": {"other", "specified", "dissociative", "disorder"},
        "unspecified dissociative disorder": {"unspecified", "dissociative", "disorder"},

        ##### Feeding and Eating Disorders:
        "feeding and eating disorders":{"feeding","eating","disorder"},
        "pica": {"pica"},
        "rumination disorder": {"rumination", "disorder"},
        "avoidant/restrictive food intake disorder": {"avoidant", "restrictive", "food", "intake", "disorder"},
        "anorexia nervosa": {"anorexia", "nervosa"},
        "bulimia nervosa": {"bulimia", "nervosa"},
        "binge-eating disorder": {"binge-eating", "disorder"},
        "other specified feeding or eating disorder": {"other", "specified", "feeding", "eating", "disorder"},
        "unspecified feeding or eating disorder": {"unspecified", "feeding", "eating", "disorder"},

        # Elimination Disorders:
        "elimination disorders": {"elimination", "disorder"},
        "enuresis": {"enuresis"},
        "encopresis": {"encopresis"},
        "other specified elimination disorder": {"other", "specified", "elimination", "disorder"},
        "unspecified elimination disorder": {"unspecified", "elimination", "disorder"},

        # Sleep-Wake Disorders:
        "sleep-wake disorder": {"sleep-wake", "disorder"},
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
        "sexual dysfunctions" : {"sexual","dysfunctions"},
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
        "gender dysphoria": {"gender", "dysphoria"},
        "gender dysphoria in children": {"gender", "dysphoria", "children"},
        "gender dysphoria in adolescents and adults": {"gender", "dysphoria", "adolescents", "adults"},
        "other specified gender dysphoria": {"other", "specified", "gender", "dysphoria"},
        "unspecified gender dysphoria": {"unspecified", "gender", "dysphoria"},

        # Disruptive, Impulse-Control, and Conduct Disorders:
        "disruptive, impulse-control, and conduct disorders" : {"disruptive", "impulse-control", "conduct", "disorder"},
        "oppositional defiant disorder": {"oppositional", "defiant", "disorder"},
        "intermittent explosive disorder": {"intermittent", "explosive", "disorder"},
        "conduct disorder": {"conduct", "disorder"},
        "pyromania": {"pyromania"},
        "kleptomania": {"kleptomania"},
        "other specified disruptive, impulse-control, and conduct disorder": {"other", "specified", "disruptive", "impulse-control", "conduct", "disorder"},
        "unspecified disruptive, impulse-control, and conduct disorder": {"unspecified", "disruptive", "impulse-control", "conduct", "disorder"},

        # Substance-Related and Addicted Disorders:
        "substance-related and addicted disorders" : {"substance-related", "and","addicted", "disorder"},
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
        "neurocognitive disorders": {"neurocognitive", "disorder"},
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
        "additional neurocognitive conditions": {"additional", "neurocognitive", "condition"},
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
        "paraphilic disorders" : {"paraphilic", "disorders"},
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
        "other mental disorders and additional codes" : {"other", "mental", "disorders","and", "additional","codes"},
        "other specified mental disorder": {"other", "specified", "mental", "disorder"},
        "unspecified mental disorder": {"unspecified", "mental", "disorder"},
        "no diagnosis or condition": {"no", "diagnosis", "condition"},

        # Medication-Induced Movement Disorders and Other Adverse Effects of Medication:
        "medication-induced movement disorders and other adverse effects of medication" : {"medication", "induced", "movement", "disorders", "and", "other", "adverse", "effects", "of", "medication"},
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


    disorder_descriptions_maps = {
        # Neurodevelopmental disorders:
        "neurodevelopmental disorders":"a group of conditions with onset in the developmental period. The disorders typically \nmanifest early in development, often before the child enters school, and are \ncharacterized by developmental deficits that produce impairments of personal, social, academic, or occupational functioning. The range of \ndevelopmental deficits varies from very specific limitations of learning or control of executive functions to \nglobal impairments of social skills or intelligence",
        "intellectual developmental disorder (intellectual disability)": "Defined by deficits in both intellectual functions \n(like reasoning, problem-solving) and adaptive functioning (like communication, \nindependent living), with onset during the developmental period",
        "global developmental delay": "Reserved for individuals under the age of 5 years when clinical severity cannot be \nreliably assessed. It is diagnosed when a child fails to meet expected developmental \nmilestones in several areas of intellectual functioning.",
        "unspecified intellectual disability (intellectual developmental disorder)": "Used when the diagnosis of intellectual \ndisability is presumed, but the individual is over the age of 5 years and it is \ndifficult to assess the severity of the disability, possibly due to associated sensory or physical impairments.",
        "langauge disorder": "Characterized by persistent difficulties in the acquisition and use of language across modalities \ndue to deficits in comprehension or production, impacting communication, social \nparticipation, academic achievement, or occupational performance.",
        "speech sound disorder": "Persistent difficulty with speech sound production that interferes with speech intelligibility \nor prevents verbal communication of messages.",
        "childhood-onset fluency disorder (stuttering)": "Characterized by disturbances in the normal fluency and time patterning \nof speech, which are inappropriate for the individual’s age and language skills, \npersist over time, and cause anxiety about speaking.",
        "pragmatic (social) communication disorder": "Characterized by primary difficulty with pragmatics, or the social use of \nlanguage and communication. Deficits lead to challenges in following social rules of \ncommunication, storytelling, or understanding language's contextual nuances.",
        "autism spectrum disorder": "A disorder characterized by persistent deficits in social communication and social \ninteraction across multiple contexts, along with restricted, repetitive patterns of behavior, \ninterests, or activities, with symptoms present in the early developmental period.",
        "attention-deficit/hyperactivity disorder (ADHD)": "A persistent pattern of inattention and/or hyperactivity-impulsivity \nthat interferes with functioning or development, with symptoms present before age 12 \nand in multiple settings.",
        "specific learning disorder": "Characterized by difficulties learning and using academic skills, with the presence \nof at least one symptom that has persisted for at least 6 months, despite interventions \ntargeting those difficulties.",
        "developmental coordination disorder": "Characterized by marked impairment in the development of motor coordination, \nsignificantly interfering with daily living activities and academic achievement, not \nattributable to a medical condition or intellectual disability.",
        "sterotypic movement disorder": "Involves repetitive, seemingly driven, and purposeless motor behavior (e.g., hand \nflapping, body rocking) that interferes with social, academic, or other activities and \nmay result in self-injury.",
        "tic disorder": "Includes conditions like Tourette's Disorder, characterized by multiple motor and one or more vocal \ntics present for more than one year, with onset before age 18.",

        # Anxiety Disorders:
        "anxiety disorders" :"Anxiety disorders involve excessive fear and anxiety, with fear being a response to \nimminent threats and anxiety related to anticipation of future threats. Fear triggers fight-or-flight \nresponses, while anxiety leads to muscle tension, vigilance, and avoidant behaviors.",
        "social anxiety disorder": "Social Anxiety Disorder is defined as a marked or intense fear or anxiety of social \nsituations in which the individual may be scrutinized by others. This anxiety can involve \na fear of being judged as anxious, weak, or unlikable, and it typically leads to\n avoidance of social situations or enduring them with significant distress.",
        "separation anxiety disorder": "Characterized by excessive fear or anxiety concerning separation from home or \nattachment figures that is developmentally inappropriate. This includes distress when separation \nis anticipated, worry about losing major attachment figures, or reluctance to be alone.",
        "selective mutism": "A consistent failure to speak in specific social situations where there is an expectation \nfor speaking (e.g., at school) despite speaking in other situations. This condition interferes \nwith educational or occupational achievement and social communication.",
        "specific phobia": "Marked fear or anxiety about a specific object or situation (e.g., flying, heights, animals) \nthat is out of proportion to the actual danger posed by the specific object or situation and \ntypically lasts for six months or more.",
        "panic disorder": "Recurrent unexpected panic attacks, which are abrupt surges of intense fear or discomfort that \nreach a peak within minutes, accompanied by physical and cognitive symptoms such as \npalpitations, sweating, shaking, shortness of breath, feelings of unreality, or fear of dying.",
        "panic attack specifier": "Refers to the occurrence of a panic attack, which is defined by an abrupt surge of intense \nfear or discomfort that reaches a peak within minutes and includes at least four \nof the 13 symptoms such as heart palpitations, sweating, trembling, shortness of breath,\n and fear of losing control or dying.",
        "agoraphobia": "Marked fear or anxiety about two or more of the following five situations: using public transportation, \nbeing in open spaces, being in enclosed places, standing in line or being in a \ncrowd, or being outside of the home alone. The individual avoids these situations because\n they believe escape might be difficult or help might not be available in the event of panic-like symptoms.",
        "generalized anxiety disorder": "Excessive anxiety and worry, occurring more days than not for at least six months, \nabout a number of events or activities. The individual finds it difficult to control \nthe worry, and the anxiety is associated with symptoms such as restlessness, fatigue,\n difficulty concentrating, irritability, muscle tension, and sleep disturbance.",
        "substance / medication induced anxiety disorder": "Anxiety or panic attacks that develop during or soon after \nsubstance intoxication or withdrawal, or after exposure to a medication, and are attributable \nto the physiological effects of the substance/medication.",
        "anxiety disorder due to another medical condition": "Clinically significant anxiety that is judged to be directly \ncaused by another medical condition, as evidenced by history, physical examination, or \nlaboratory findings.",
        "other specified anxiety disorder": "This category applies to presentations of anxiety symptoms that cause clinically \nsignificant distress or impairment but do not meet the full criteria for any of the \nother anxiety disorders. The clinician provides a specific reason why the \npresentation does not meet the criteria.",

        # Depressive Disorders:
        "depressive disorders" :"Depressive Disorders include major depressive disorder, persistent depressive \ndisorder, premenstrual dysphoric disorder, and others. All share a sad, empty, \nor irritable mood with changes that impair the individual's ability to function.",
        "chronic depressive disorder": "Chronic Depressive Disorder (CDD) is a persistent and long-term form of depression \nwhere symptoms are less severe but last for an extended period, often for years.",
        "disruptive mood dysfunction": "Defined by chronic, severe, and persistent irritability, with frequent temper outbursts \nthat are disproportionate in intensity or duration to the situation. The irritability \nmust be present most of the day, nearly every day, between outbursts.",
        "major depressive disorder": "Characterized by a persistent and pervasive depressed mood or loss of interest or pleasure \nin nearly all activities. This disorder includes other symptoms such as significant \nweight changes, sleep disturbances, fatigue, feelings of worthlessness or excessive \nguilt, difficulty concentrating, and recurrent thoughts of death or suicide ",
        "persistent depressive disorder (dysthymia)": "A chronic form of depression where a person experiences a depressed \nmood for most of the day, for more days than not, for at least two years (or one year for \nchildren and adolescents). Symptoms may include poor appetite, insomnia or hypersomnia, \nlow energy or fatigue, low self-esteem, poor concentration, and feelings of hopelessness.",
        "premenstrual dysphoric disorder": "This disorder is marked by mood lability, irritability, dysphoria, and anxiety \nthat occur repeatedly during the premenstrual phase of the menstrual cycle and remit around \nthe onset of menses or shortly thereafter. These mood symptoms must significantly \ninterfere with work, school, or usual social activities and relationships.",
        "substance/medication-induced depressive disorder": "A depressive disorder caused by the use of or withdrawal from a \nsubstance or medication. The symptoms are characterized by a prominent and persistent \ndisturbance in mood, primarily involving depressed mood or loss of interest or pleasure in almost all activities.",
        "depressive disorder due to another medical condition": "A depressive disorder that is directly attributable to the \nphysiological effects of another medical condition. The mood disturbance may involve \ndepressed mood or markedly diminished interest or pleasure in all, or almost all, activities.",
        "other specified depressive disorder": "This category is used when depressive symptoms cause significant distress or \nimpairment but do not meet the full criteria for any other depressive disorder. The \nclinician specifies the reason that the presentation does not meet the criteria for another depressive disorder.",
        "unspecified depressive disorder": "Used when depressive symptoms cause significant distress or impairment but do not \nmeet the criteria for any specific depressive disorder, and the clinician chooses not \nto specify the reason, or there is insufficient information to make a more specific diagnosis.",

        # Schizophrenia and other Psychotic Disorders
        "schizophrenia and other psychotic disorders" : "Schizophrenia Spectrum and Other Psychotic Disorders include \nschizophrenia, other psychotic disorders, and schizotypal disorder. They are characterized by \nabnormalities in delusions, hallucinations, disorganized thinking, disorganized behavior, and negative symptoms.",
        "schizotypal (personality) disorder": "Characterized by pervasive patterns of social and interpersonal deficits, \nincluding discomfort with close relationships, as well as cognitive or perceptual distortions \nand eccentric behaviors. Individuals may exhibit odd beliefs, magical thinking, and social anxiety.",
        "delusional disorder": "Involves the presence of one or more delusions (false beliefs) that persist for at least \none month. Apart from the delusions, the person's functioning is not markedly impaired, and \nbehavior is not obviously bizarre or odd.",
        "brief psychotic disorder": "A short-term psychotic disorder lasting more than one day but less than one month, \nwith a sudden onset of at least one of the following: delusions, hallucinations, disorganized \nspeech, or grossly disorganized or catatonic behavior.",
        "schizophreniform": "Similar to schizophrenia, but with a shorter duration of symptoms, lasting at least one month \nbut less than six months. It includes symptoms like delusions, hallucinations, disorganized \nspeech, and negative symptoms (e.g., diminished emotional expression).",
        "schizophrenia": "A severe mental disorder characterized by a range of symptoms, including delusions, hallucinations, \ndisorganized thinking, grossly disorganized or abnormal motor behavior (including catatonia), \nand negative symptoms. These symptoms must persist for at least six months.",
        "schizoaffective disorder": "Features a combination of schizophrenia symptoms (like delusions or hallucinations) and \nmood disorder symptoms (either depressive or manic episodes). The psychotic features must be \npresent for a significant portion of the illness duration, even outside of mood episodes.",
        "substance/medication-induced psychotic disorder": "Psychotic symptoms, such as delusions or hallucinations, are \ncaused by the use of or withdrawal from a substance or medication. The symptoms typically emerge \nduring or shortly after substance use.",
        "psychotic disorder due to another medical condition": "Psychotic symptoms (delusions or hallucinations) are directly \nattributable to another medical condition. The diagnosis is confirmed through clinical \nassessment and testing.",
        "catatonia associated with another mental disorder (catatonia specifier)": "A syndrome of psychomotor disturbances \nassociated with various mental disorders, including schizophrenia. Symptoms can include stupor, \nmutism, negativism, posturing, and rigidity.",
        "catatonic disorder due to another medical condition": "Catatonia that is directly attributable to a medical condition, \nas evidenced by clinical examination and diagnostic testing.",
        "other specified schizophrenia spectrum and other psychotic disorder": "This category is used when psychotic symptoms \ncause significant distress or impairment but do not meet the full criteria for any specific \ndisorder in the schizophrenia spectrum. The clinician specifies the reason why the criteria are not fully met.",
        "unspecified schizophrenia spectrum and other psychotic disorder": "Used when psychotic symptoms cause significant \ndistress or impairment, but there is insufficient information to make a more specific diagnosis, \nor the clinician chooses not to specify the reason.",
        "unspecified catatonia": "Used when the clinical presentation suggests the presence of catatonia, but there is \ninsufficient information to determine the specific cause or associated condition.",

        # Bipolar Disorders and Related Disorders:
        "bipolar disorders and related disorders" : "Bipolar and related disorders are placed between schizophrenia spectrum and other psychotic disorders and depressive disorders in DSM-5-TR in recognition of their place as \na bridge between those two diagnostic classes in terms of symptomatology, \nfamily history, and genetics.",
        "bipolar I(1) disorder": "Defined by the occurrence of at least one manic episode, which may be preceded by and\n possibly followed by hypomanic or major depressive episodes. A manic episode involves a distinct period\n of abnormally and persistently elevated, expansive, or irritable mood, \nand increased activity or energy.",
        "bipolar II(2) disorder": "Characterized by a pattern of depressive episodes and hypomanic episodes, but not the\n full-blown manic episodes that are typical of Bipolar I Disorder. The hypomanic episodes in\n Bipolar II Disorder do not cause the same level of impairment as the manic episodes \nin Bipolar I.",
        "cyclothymic disorder": "Involves numerous periods of hypomanic symptoms and periods of depressive symptoms that\n do not meet the criteria for a hypomanic episode or a major depressive episode. These symptoms occur\n for at least two years in adults (one year in children and adolescents) and \nare persistent, with symptom-free intervals lasting no longer than two months.",
        "substance / medication-induced bipolar and related disorder": "Involves a prominent and persistent disturbance\n in mood that is characterized by an abnormally elevated, expansive, or irritable mood, with or without\n depressed mood, and an abnormally increased activity or energy. This mood \ndisturbance is due to the direct physiological effects of a substance or medication.",
        "bipolar and related disorder due to another medical condition": "This disorder involves a mood disturbance,\n characterized by abnormally elevated, expansive, or irritable mood, and increased activity or energy, that\n is directly attributable to another medical condition.",
        "other specified bipolar and related disorder": "This category is used for conditions in which symptoms\n characteristic of bipolar and related disorders cause significant distress or impairment in social, occupational,\n or other important areas of functioning but do not meet the full criteria \nfor any specific bipolar disorder. The clinician provides the specific reason why the criteria are not met.",
        "unspecified bipolar and related disorder": "Used when the clinician chooses not to specify the reason that\n the criteria are not met for a specific bipolar disorder, or there is insufficient information to make a more\n specific diagnosis.",

        # obsessive-compulsive disorder (ocd):
        "obsessive - compulsive disorder (OCD)": "Characterized by the presence of obsessions (recurrent and persistent\n thoughts, urges, or images) and/or compulsions (repetitive behaviors or mental acts) that are time-consuming\n (taking more than one hour per day) or cause significant distress or impairment.",
        "body dysmorphic disorder": "Involves a preoccupation with one or more perceived defects or flaws in physical\n appearance that are not observable or appear slight to others. This preoccupation leads to repetitive behaviors\n (e.g., mirror checking, excessive grooming) or mental acts (e.g., comparing appearance with others).",
        "hoarding disorder": "Persistent difficulty discarding or parting with possessions, regardless of their actual\n value, due to a perceived need to save them and distress associated with discarding them. This behavior results\n in the accumulation of possessions that clutter living areas and \nsubstantially compromise their intended use.",
        "trichotillomania (hair - pulling disorder)": "Recurrent pulling out of one's hair, leading to hair loss,\n accompanied by repeated attempts to decrease or stop the behavior. The hair pulling causes clinically significant\n distress or impairment in functioning.",
        "excoriation (skin - picking) disorder": "Recurrent skin picking resulting in skin lesions, accompanied by\n repeated attempts to decrease or stop the behavior. The skin picking causes clinically significant distress or\n impairment in functioning.",
        "substance / medication - induced obsessive - compulsive and related disorder": "Obsessive-compulsive symptoms\n that are caused by the use of or withdrawal from a substance or medication. The symptoms are directly attributable\n to the substance or medication involved.",
        "obsessive - compulsive and related disorder due to another medical condition": "Obsessive-compulsive symptoms\n that are directly attributable to the physiological effects of another medical condition. This diagnosis is made\n based on clinical assessment and testing.",
        "other specified obsessive - compulsive and related disorder": "This category is used when symptoms characteristic\n of an obsessive-compulsive and related disorder cause significant distress or impairment in functioning but\n do not meet the full criteria for any specific disorder in this category. \nThe clinician specifies the reason why the criteria are not fully met.",
        "unspecified obsessive - compulsive and related disorder": "Used when obsessive-compulsive symptoms cause significant\n distress or impairment but do not meet the criteria for any specific disorder in this category, and the\n clinician chooses not to specify the reason, or there is insufficient \ninformation to make a more specific diagnosis.",

        # Trauma and Stressor - related:
        "trauma and stressor-related" : "Trauma- and stressor-related disorders include disorders in which exposure to a \ntraumatic or stressful event is listed explicitly as a diagnostic criterion. These include reactive attachment \ndisorder, disinhibited social engagement disorder, posttraumatic stress disorder \n(PTSD), acute stress disorder, adjustment disorders, and prolonged grief disorder",
        "reactive attachment disorder": "Characterized by a pattern of markedly disturbed and developmentally inappropriate\n attachment behaviors in which a child rarely or minimally turns preferentially to an attachment figure for\n comfort, support, protection, and nurturance. This disorder is associated \nwith social neglect or other situations that limit opportunities to form selective attachments.",
        "disinhibited social engagement disorder": "Involves a pattern of behavior in which a child actively approaches and\n interacts with unfamiliar adults and exhibits overly familiar verbal or physical behavior that violates\n social boundaries. This disorder often arises from social neglect or a lack of \nconsistent caregiving",
        "posttraumatic stress disorder [PTSD]": "A condition triggered by exposure to a traumatic event, characterized by\n symptoms such as intrusive thoughts, flashbacks, avoidance of reminders of the trauma, negative changes in\n thoughts and mood, and heightened arousal and reactivity. PTSD symptoms must \npersist for more than one month and cause significant distress or impairment.",
        "acute stress disorder": "Similar to PTSD, this disorder occurs shortly after a traumatic event and includes symptoms\n like dissociation, intrusive memories, avoidance, and hyperarousal. The key difference is that symptoms\n last for a shorter period—between 3 days and 1 month after the trauma.",
        "adjustment disorder": "A condition where the grieving process is prolonged, lasting beyond the expected time frame,\n with intense yearning or longing for the deceased, preoccupation with the deceased, and significant disruption\n in personal, family, or occupational functioning.",
        "prolonged grief disorder": "A condition where the grieving process is prolonged, lasting beyond the expected time frame,\n with intense yearning or longing for the deceased, preoccupation with the deceased, and significant\n disruption in personal, family, or occupational functioning.",
        "other specific trauma- and stressor-related disorder": "Used when trauma-related symptoms cause significant distress or\n impairment but do not meet the full criteria for any specific trauma- or stressor-related disorder.\n The clinician specifies the reason why the criteria are not met.",
        "unspecified trauma- and stressor- related disorder": "This category is used when symptoms of a trauma- or stressor-related\n disorder cause significant distress or impairment, but there is insufficient information to specify\n the diagnosis or the clinician chooses not to specify the reason why the criteria are not met.",

        # dissociative disorders:
        "dissociative disorders" : "Dissociative disorders are characterized by a disruption of and/or discontinuity in the normal \nintegration of consciousness, memory, identity, emotion, perception, body representation, motor \ncontrol, and behavior. Dissociative symptoms can potentially disrupt every area \nof psychological functioning",
        "dissociative identity disorder": "Characterized by the presence of two or more distinct personality states or an experience\n of possession, with marked discontinuity in sense of self and sense of agency, accompanied by \nrelated alterations in affect, behavior, consciousness, memory, perception, \ncognition, and/or sensory-motor functioning. These symptoms may be observed by others or reported by the individual.",
        "dissociative amnesia": "Involves an inability to recall important autobiographical information, usually of a traumatic or\n stressful nature, that is inconsistent with ordinary forgetting. This can manifest as localized \n(failure to recall events during a specific period), selective (failure to \nrecall some but not all events during a period), or generalized (complete loss of memory for one’s life history).",
        "depersonalization/derealization disorder": " Characterized by persistent or recurrent experiences of depersonalization (detachment\n or feeling of being an outside observer to one’s thoughts, feelings, body, or actions) \nand/or derealization (experiences of unreality or detachment with respect to \nsurroundings). During these experiences, reality testing remains intact.",
        "other specified dissociative disorder": "This category applies to presentations in which symptoms characteristic of a dissociative\n disorder cause clinically significant distress or impairment but do not meet the full \ncriteria for any of the specific dissociative disorders. The specific reason for \nthe presentation not meeting the full criteria is communicated, such as 'dissociative trance''.",
        "unspecified dissociative disorder": "Used when symptoms characteristic of a dissociative disorder cause significant distress or\n impairment but do not meet the full criteria for any specific dissociative disorder. This \ncategory is used when the clinician chooses not to specify the reason the criteria \nare not met or when there is insufficient information to make a more specific diagnosis.",
        # somatic symptom and related disorders:
        "somatic symptom and related disorders" : "Somatic Symptom and Related Disorders include diagnoses such as somatic symptom \ndisorder, illness anxiety disorder, functional neurological symptom disorder (conversion disorder), \npsychological factors affecting other medical conditions, factitious disorder, other \nspecified somatic symptom and related disorder, and unspecified somatic symptom and related disorder. \nThese disorders share a common feature: the prominence \nof somatic symptoms and/or illness anxiety associated with significant distress and impairment",
        "somatic symptom disorder": "Somatic symptom disorder is characterized by somatic symptoms that are distressing or result in \nsignificant disruption of daily life, accompanied by excessive thoughts, feelings, or behaviors \nrelated to these symptoms or associated health concerns as manifested by at least one of the following:\nDisproportionate and persistent thoughts about the seriousness of one's symptoms.\nPersistently high level of anxiety about health or symptoms.\nExcessive time and energy devoted to these symptoms or health concerns.",
        "illness (anxiety) disorder": "Illness anxiety disorder is preoccupation with having or acquiring a serious illness. Somatic \nsymptoms are not present, or if present, are only mild in intensity. If another medical condition \nis present or there is a high risk for developing a medical condition, the preoccupation\n is clearly excessive or disproportionate.",
        "conversion disorder (functional neurological symptom disorder)": "Conversion disorder (functional neurological symptom disorder) \nis characterized by one or more symptoms of altered voluntary motor or sensory function. Clinical \nfindings provide evidence of incompatibility between the symptom and recognized\n neurological or medical conditions.",
        "(somatic) psychological factors affecting other medical condtions ": "Psychological factors affecting other medical conditions is \ncharacterized by the presence of one or more clinically significant psychological or behavioral \nfactors that adversely affect a medical condition by increasing the risk for\n suffering, death, or disability.",
        "factitious disorder": "Factitious disorder involves the falsification of medical or psychological signs and symptoms in oneself or \nothers that are associated with the identified deception. The individual presents themselves to \nothers as ill, impaired, or injured.",
        "other specified somatic symptoms and related disorder": "This category applies to presentations in which symptoms characteristic of a \nsomatic symptom and related disorder that cause clinically significant distress or impairment \nin social, occupational, or other important areas of functioning predominate but do not meet\n the full criteria for any of the disorders in the somatic symptom and related disorders diagnostic class.",
        "unspecified somatic symptoms and related disorder": "Unspecified Somatic Symptom and Related Disorder applies when symptoms cause \nsignificant distress or impairment but don’t fully meet the criteria for a specific disorder. This category \nis used when the clinician opts not to specify the reason or lacks enough information for a more precise diagnosis.",

        # feeding and eating disorders:
        "feeding and eating disorders" : "Feeding and eating disorders are characterized by a persistent disturbance of eating or \neating-related behavior that results in the altered consumption or absorption of food and that significantly \nimpairs physical health or psychosocial functioning",
        "pica": "The essential feature of pica is the eating of one or more nonnutritive, nonfood substances on a persistent basis over a \nperiod of at least 1 month, that is severe enough to warrant clinical attention.",
        "rumination disorder": "The essential feature of rumination disorder is the repeated regurgitation of food occurring after feeding or\n eating over a period of at least 1 month. The food may be re-chewed, re-swallowed, or spit out.",
        "avoidant/restrictive food intake disorder": "Avoidant/restrictive food intake disorder is characterized by avoidance or restriction of\n food intake that is associated with one (or more) of the following consequences:\n1.Significant weight loss (or failure to achieve expected weight gain or faltering growth in children).\n2.Significant nutritional deficiency.\n3.Dependence on enteral feeding or oral nutritional supplements.\n4.Marked interference with psychosocial functioning.",
        "anorexia nervosa": "Anorexia nervosa is characterized by persistent energy intake restriction; intense fear of gaining weight or of \nbecoming fat, or persistent behavior that interferes with weight gain; and a disturbance in \nself-perceived weight or shape.",
        "bulimia nervosa": "Bulimia nervosa is defined by recurrent episodes of binge eating characterized by both of the following:\n1.Eating, in a discrete period of time, an amount of food that is definitely larger than what most \nindividuals would eat in a similar period under similar circumstances.\n2.A sense of lack of control over eating during the episode (e.g., a feeling that one cannot stop eating or control what or how much one is eating).",
        "binge-eating disorder": "Binge-eating disorder is characterized by recurrent episodes of binge eating. An episode of binge eating is \ncharacterized by both of the following:\n1.Eating, in a discrete period of time, an amount \nof food that is definitely larger than what most people would eat in a similar period under similar circumstances.\n2.A sense of lack of control over eating during the episode.",
        "other specified feeding or eating disorder": "Other Specified Feeding or Eating Disorder applies when symptoms cause significant \ndistress or impairment but don't fully meet the criteria for a specific disorder. This category is \nused when the clinician specifies why the criteria are not fully met.",
        "unspecified feeding or eating disorder": "Unspecified Feeding or Eating Disorder applies when symptoms cause significant distress \nor impairment but don't meet full criteria for a specific disorder. This category is used when the \nclinician doesn't specify the reason or lacks enough information for a more precise diagnosis.",
        # elimination disorders:
        "elimination disorders" : "Elimination disorders all involve the inappropriate elimination of urine or feces and are usually first diagnosed in \nchildhood or adolescence. This group of disorders includes enuresis (the repeated \nvoiding of urine into inappropriate places) and encopresis (the repeated \npassage of feces into inappropriate places)",
        "enuresis": "This involves repeated voiding of urine into inappropriate places (e.g., bed or clothes). It can be classified based on the time of occurrence:\nNocturnal only (during sleep)\nDiurnal only (during waking hours)\nNocturnal and diurnal",
        "encopresis": "This involves the repeated passage of feces into inappropriate places (e.g., clothing or floor). It is specified by:\nWith constipation and overflow incontinence\nWithout constipation and overflow incontinence",
        "other specified elimination disorder": "This category is used when symptoms cause significant distress or impairment but do not meet the full criteria for any specific elimination disorder. The specific reason for not meeting the criteria is usually documented (e.g., low-frequency enuresis).",
        "unspecified elimination disorder": "This is used when symptoms characteristic of an elimination disorder are present, causing significant\n distress or impairment, but there is insufficient information to make a more \nspecific diagnosis (e.g., in emergency room settings).",

        # sleep - wake disorders (page 407-page 477):
        "sleep-wake disorders" : "Sleep-Wake Disorders involve complaints about the quality, timing, and amount of sleep, leading to daytime \ndistress and impaired functioning. This category includes disorders such as insomnia \ndisorder, hypersomnolence disorder, narcolepsy, breathing-related sleep disorders, \ncircadian rhythm sleep-wake disorders, parasomnias, and sleep-related movement disorders",
        "insomnia disorder": "Dissatisfaction with sleep quantity or quality, associated with one (or more) of the following symptoms: \ndifficulty initiating sleep; \ndifficulty maintaining sleep; \nearly-morning awakening with inability to return to sleep",
        "hypersomnolence disorder": "Self-reported excessive sleepiness (hypersomnolence) despite a main sleep period lasting at least 7 hours, \nwith at least one of the following symptoms: recurrent periods of sleep or lapses\n into sleep within the same day; a prolonged main sleep episode of more than 9 hours per day that is \nnonrestorative; difficulty being fully awake after abrupt awakening",
        "narcolepsy": "Recurrent periods of an irrepressible need to sleep, lapsing into sleep, or napping occurring within the same day",
        "obstructive sleep apnea hypopnea": "Repeated episodes of upper (pharyngeal) airway obstruction (apneas and hypopneas) during sleep",
        "central sleep apnea": "Repetitive episodes of apneas and hypopneas during sleep caused by variability in respiratory effort",
        "sleep-related hypoventilation": "Episodes of decreased respiration associated with elevated CO2 levels that occur during sleep",
        "circadian rhythm sleep-wake disorder": "Persistent or recurrent pattern of sleep disruption that is primarily due to an alteration \nof the circadian system or to a misalignment between the endogenous circadian rhythm and \nthe sleep-wake schedule required by an individual's physical environment or social or professional schedule",
        "non-rapid eye movement (non-REM) sleep arousal": "Recurrent episodes of incomplete awakening from sleep, usually occurring during \nthe first third of the major sleep episode, accompanied by either sleepwalking or sleep terrors",
        "nightmare disorder": "Repeated occurrences of extended, extremely dysphoric, and well-remembered dreams that usually involve efforts \nto avoid threats to survival, security, or physical integrity",
        "rapid eye movement (REM) sleep behavior disorder": "Repeated episodes of arousal during sleep associated with vocalization and/or \ncomplex motor behaviors",
        "restless legs syndrome": "An urge to move the legs, usually accompanied by or in response to uncomfortable and unpleasant sensations \nin the legs",
        "substance/medication-induced sleep disorder": "A prominent sleep disturbance that is sufficiently severe to warrant independent \nclinical attention",
        "other specified sleep-wake disorder": "Symptoms characteristic of a sleep-wake disorder that cause clinically significant distress \nor impairment in social, occupational, or other important areas of functioning but do not \nmeet the full criteria for any of the disorders in the sleep-wake disorders diagnostic class",
        "unspecified sleep-wake disorder": "Symptoms characteristic of a sleep-wake disorder that cause clinically significant distress or \nimpairment in social, occupational, or other important areas of functioning but do not meet \nthe full criteria for any of the disorders in the sleep-wake disorders diagnostic class",

        # sexual dysfunctions (page 477- page 511):
        "sexual dysfunctions" : "Sexual dysfunctions are a heterogeneous group of disorders that are typically characterized by a clinically \nsignificant disturbance in a person’s ability to respond sexually or to experience sexual \npleasure. An individual may have several sexual dysfunctions at the same time. In such cases, all of the dysfunctions should be diagnosed",
        "delayed ejaculation": "Difficulty in or inability to achieve ejaculation during partnered sexual activity.",
        "erectile disorder": "Difficulty in obtaining or maintaining an erection during sexual activity or marked decrease in erectile rigidity.",
        "female orgasmic disorder": "Delay in, infrequency of, or absence of orgasm or reduced intensity of orgasmic sensations.",
        "female sexual interest/arousal disorder": "Lack of or significantly reduced sexual interest/arousal as manifested by at least \nthree of several possible symptoms (e.g., absent/reduced interest in sexual activity, \nabsent/reduced sexual/erotic thoughts or fantasies).",
        "genito-pelvic pain/penetration disorder": "Difficulties with vaginal penetration, vulvovaginal or pelvic pain during intercourse, \nfear or anxiety about pain in anticipation of, during, or as a result of vaginal \npenetration, or tensing or tightening of the pelvic floor muscles during attempted vaginal penetration.",
        "male hypoactive sexual desire disorder": "Persistently or recurrently deficient (or absent) sexual/erotic thoughts or fantasies and \ndesire for sexual activity.",
        "premature (early) ejaculation": "A pattern of ejaculation occurring during partnered sexual activity within approximately 1 minute \nfollowing vaginal penetration and before the individual wishes it.",
        "substance/medication-induced sexual disorder": "Sexual dysfunctions associated with substance use, including alcohol, opioids, \nsedatives, hypnotics, anxiolytics, stimulants, and other substances.",
        "other specified sexual dysfunction": "Symptoms characteristic of a sexual dysfunction that cause clinically significant distress \nbut do not meet the full criteria for any of the disorders in the sexual \ndysfunctions diagnostic class.",
        "unspecified sexual dysfunctional": "Symptoms characteristic of a sexual dysfunction that cause clinically significant distress but \ndo not meet the full criteria for any of the disorders in the sexual \ndysfunctions diagnostic class",

        # gender dysphoria (page 511- page 521):
        "gender dysphoria" : "Gender dysphoria refers to the distress that may accompany the incongruence between one's experienced \nor expressed gender and one's assigned gender. This condition causes clinically \nsignificant distress or impairment in social, occupational, or other important areas of functioning",
        "gender dysphoria in children": "A marked incongruence between one’s experienced/expressed gender and assigned gender, \nlasting at least 6 months, and manifested by a strong desire to be of the other gender \nor insistence that one is the other gender, along with other criteria.",
        "gender dysphoria in adolescents and adults": "A marked incongruence between one’s experienced/expressed gender and \nassigned gender, lasting at least 6 months, with at least two of several possible criteria \n(e.g., a strong desire to be rid of one’s primary and/or secondary sex characteristics).",
        "other specified gender dysphoria": "This category applies to presentations where symptoms characteristic of gender \ndysphoria cause clinically significant distress or impairment but do not meet the full \ncriteria for gender dysphoria. The specific reason for not meeting the criteria is usually documented.",
        "unspecified gender dysphoria": "This category is used when symptoms characteristic of gender dysphoria cause \nclinically significant distress or impairment but do not meet the full criteria for gender \ndysphoria, and there is insufficient information to make a more specific diagnosis.",

        # disruptive, impulse-control, and conduct disorders (page 521- page 543):
        "disruptive, impulse-control, and conduct disorders" : "Disruptive, impulse-control, and conduct disorders \ninclude conditions involving problems in the self-control of emotions and behaviors. These \nproblems are manifested in behaviors that violate the rights of others (e.g., aggression, destruction of property) \nand/or that bring the individual into significant conflict with societal norms or authority figures",
        "oppositional defiant disorder": "A pattern of angry/irritable mood, argumentative/defiant behavior, or \nvindictiveness lasting at least 6 months.",
        "intermittent explosive disorder": "Recurrent behavioral outbursts representing a failure to control \naggressive impulses as manifested by verbal or physical aggression.",
        "conduct disorder": "A repetitive and persistent pattern of behavior in which the basic rights of \nothers or major age-appropriate societal norms or rules are violated.",
        ##"antisocial personality disorder":"A pervasive pattern of disregard for and violation of the rights of others, occurring since age 15 years.",
        "pyromania": " Deliberate and purposeful fire setting on more than one occasion.",
        "kleptomania": "Recurrent failure to resist impulses to steal objects that are not needed for \npersonal use or for their monetary value.",
        "other specified disruptive, impulse-control, and conduct disorder": "Symptoms characteristic of a disruptive, impulse-control, and \nconduct disorder that cause significant distress or impairment \nbut do not meet the full criteria for any of the disorders in this diagnostic class.",
        "unspecified disruptive, impulse-control, and conduct disorder": "Symptoms characteristic of a disruptive, impulse-control, and conduct \ndisorder that cause significant distress or impairment but \ndo not meet the full criteria for any of the disorders in this diagnostic class, with the specific reason not specified.",

        # substance-related and addicted disorders(page 543 - page 667):
        "substance-related and addicted disorders" : "Substance-Related Disorders include \n10 classes of drugs: alcohol, caffeine, cannabis, hallucinogens (phencyclidine and others), inhalants, opioids, sedatives, stimulants, tobacco, and other substances. These drugs share the ability to activate the brain's reward system, reinforcing behaviors and forming memories.",
        "alcohol-related disorders": "Includes Alcohol Use Disorder, Alcohol Intoxication, \nAlcohol Withdrawal, and other alcohol-induced disorders.",
        "caffeine-related disorders": "Includes Caffeine Intoxication, Caffeine Withdrawal, \nand other caffeine-induced disorders.",
        "cannabis-related disorders": "Includes Cannabis Use Disorder, Cannabis Intoxication, \nCannabis Withdrawal, and other cannabis-induced disorders.",
        "hallucinogen-related disorders": "Use Disorder, Other Hallucinogen Use Disorder, \nHallucinogen Persisting Perception Disorder, and other hallucinogen-induced disorders.",
        "inhalant-related disorders": " Includes Inhalant Use Disorder and other \ninhalant-induced disorders.",
        "opioid-related disorders": "Includes Opioid Use Disorder, Opioid Intoxication, \nOpioid Withdrawal, and other opioid-induced disorders.",
        "sedative-related,hypnotic-related,or anxiolytic-related disorders": " Includes Sedative-, Hypnotic-, or Anxiolytic Use Disorder, \nIntoxication, Withdrawal, and other related induced disorders.",
        "stimulant-related disorders": "Includes Amphetamine-Type Substance, Cocaine, or Other Stimulant Use Disorder, Stimulant Intoxication, \nStimulant Withdrawal, and other stimulant-induced disorders.",
        "tobacco-related disorders": "Includes Tobacco Use Disorder, Tobacco Withdrawal, and other tobacco-induced disorders.",
        "other (or unknown) substance-related disorders": "Includes disorders related to the use of other or unknown \nsubstances not classified under the previous categories.",

        "alcohol use disorder": "A problematic pattern of alcohol use leading to clinically \nsignificant impairment or distress, as manifested by at \nleast two of several specified criteria, occurring within a 12-month period.",
        "alcohol intoxication": "Recent ingestion of alcohol leading to significant \nproblematic behavioral or psychological changes, with signs or \nsymptoms such as slurred speech, incoordination, or impaired attention.",
        "alcohol withdrawal": "Cessation or reduction in heavy and prolonged alcohol use, \nleading to specific symptoms such as autonomic hyperactivity, \nhand tremor, insomnia, or nausea.",
        "caffeine intoxication": "Recent consumption of caffeine, usually in excess of 250 mg \n(more than 2-3 cups of brewed coffee), leading to five or more specific symptoms:\n1.Restlessness\n2.Nervousness\n3.Excitement\n4.Insomnia\n5.Flushed face\n6.Diuresis (increased urination\n6.Gastrointestinal disturbance\n7.Muscle twitching\n8.Rambling flow of thought and speech\n9.Tachycardia (increased heart rate) or cardiac arrhythmia\n10.Periods of inexhaustibility (not feeling tired)\n11.Psychomotor agitation",
        "caffeine withdrawal": "Prolonged daily use of caffeine followed by abrupt cessation or \nreduction, leading to symptoms like headache, fatigue, or dysphoric mood.",
        "cannabis use disorder": "A problematic pattern of cannabis use leading to clinically \nsignificant impairment or distress, as manifested by at \nleast two of several criteria, occurring within a 12-month period.",
        "cannabis intoxication": "Recent use of cannabis leading to clinically significant \nproblematic behavioral or psychological changes, with symptoms \nsuch as conjunctival injection, increased appetite, or dry mouth.",
        "cannabis withdrawal": "Cessation of cannabis use that has been heavy and prolonged, \nleading to three or more specific symptoms, such as \nirritability, sleep difficulty, or decreased appetite.",
        "phencyclidine (PCP) use disorder": "A problematic pattern of phencyclidine use leading \nto clinically significant impairment or distress.",
        "other hallucinogen use disorder": "A problematic pattern of hallucinogen use other than \nphencyclidine, leading to clinically significant impairment or distress.",
        "inhalant use disorder": "A problematic pattern of inhalant use leading to clinically \nsignificant impairment or distress.",
        "opioid use disorder": "A problematic pattern of opioid use leading to clinically \nsignificant impairment or distress.",
        "opioid intoxication": "Recent use of an opioid leading to problematic behavioral or \npsychological changes, with specific symptoms such \nas pupillary constriction or drowsiness.",
        "opioid withdrawal": "Cessation of opioid use that has been heavy and prolonged, or \nadministration of an opioid antagonist, leading to \nspecific symptoms such as dysphoric mood, nausea, or muscle aches.",
        "sedative, hyponotic, or anxiolytic use disorder": "A problematic pattern of sedative, \nhypnotic, or anxiolytic use leading to clinically \nsignificant impairment or distress.",
        "stimulant use disorder": "A problematic pattern of stimulant use leading to clinically \nsignificant impairment or distress.",
        "tobacco use disorder": "A problematic pattern of tobacco use leading to clinically \nsignificant impairment or distress.",
        "gambling disorder": "Persistent and recurrent problematic gambling behavior leading \nto clinically significant impairment or distress, as \nindicated by the individual exhibiting four or more of several specified criteria in a 12-month period.",

        # neurocognitive disorders (page 667- page 733):
        "neurocognitive disorders" : "The neurocognitive disorders (NCDs) encompass the group \nof disorders in which the primary clinical deficit is in cognitive function and that are acquired rather than \ndevelopmental. Although cognitive deficits are present in many, if not all, mental disorders, only \ndisorders whose core features are cognitive are included in the NCD category",
        "delirium": " Characterized by a disturbance in attention and awareness that develops \nover a short period, represents a change from baseline \nattention and awareness, and tends to fluctuate in severity during \nthe course of the day.",
        "major neurocognitive disorder": "Significant cognitive decline from a previous level of \nperformance in one or more cognitive domains \n(e.g., complex attention, executive function, learning, and memory) that \ninterferes with independence in everyday activities.",
        "mild neurocognitive disorder": "Modest cognitive decline from a previous level of \nperformance in one or more cognitive domains that does not \ninterfere with capacity for independence in everyday activities but \nmay require greater effort or compensatory strategies.",
        "major or mild neurocognitive disorder due to alzheimer's disease": " A diagnosis given \nwhen the criteria for major or mild neurocognitive \ndisorder are met, with gradual onset and progressive cognitive decline, \nand Alzheimer's disease is either the probable or possible cause.",
        "major or mild frontotemporal neurocognitive disorder": "Cognitive decline is associated \nwith frontotemporal lobar degeneration, often presenting \nwith either behavioral variant or language variant.",
        "major or mild neurocognitive disorder with lewy bodies": "Progressive cognitive decline \nassociated with visual hallucinations, parkinsonism, and \nfluctuating cognition.",
        "major or mild vascular neurocognitive disorder": "Cognitive decline resulting from \ncerebrovascular events, presenting with a stepwise progression \nof cognitive deficits, often after a stroke.",
        "major or mild neurocognitive disorder due to traumatic brain injury": " Cognitive \ndecline following a traumatic brain injury, with onset of the \nneurocognitive disorder immediately after the occurrence of \nthe injury or after regaining consciousness.",
        "substance/medication-induced major or mild neurocognitive disorder": " Cognitive \ndecline related to the persistent effects of substance use or \nexposure to toxins.",
        "major or mild neurocognitive disorder due to HIV injection": "Cognitive decline \nassociated with HIV infection, not better explained by non-HIV conditions.",
        "major or mild neurocognitive disorder due to prion diseases": "Rapidly progressing \ncognitive decline caused by prion disease, such as \nCreutzfeldt-Jakob disease.",
        "major or mild neurocognitive disorder due to parkinson's disease": "Cognitive decline \nthat occurs in the context of Parkinson’s disease, \noften with a decline in executive function, attention, and memory.",
        "major or mild neurocognitive disorder due to huntington's disease": "Cognitive decline \nassociated with Huntington’s disease, typically with \nearly changes in executive function.",
        "major or mild neurocognitive disorder due to another medical condition": "Cognitive decline \ncaused by a medical condition not listed elsewhere.",
        "major or mild neurocognitive disorder due to multiple etiologies": "Cognitive decline \nresulting from more than one cause, such as Alzheimer’s \ndisease and cerebrovascular disease.",
        "unspecified neurocognitive disorder": "Used when symptoms of cognitive decline are \npresent, but there is insufficient information to\n determine the specific cause.",

        "alzheimer's disease": "A progressive neurodegenerative disease that primarily \naffects memory, thinking, and behavior. It is characterized by the \ngradual onset of cognitive impairment that worsens over time, eventually \ninterfering with daily functioning. The pathology involves amyloid plaques and neurofibrillary tangles in the brain.",
        "frontotemporal degeneration": "A group of disorders caused by progressive cell \ndegeneration in the brain's frontal or temporal lobes. It often \nresults in significant changes in personality, behavior, or language. Unlike \nAlzheimer’s, it typically affects younger adults and may present with either behavioral changes or language difficulties.",
        "lewy body disease": "A neurodegenerative disorder characterized by the presence \nof Lewy bodies (abnormal aggregates of protein) in brain cells. \nIt leads to cognitive decline, visual hallucinations, fluctuating levels of \nconsciousness, and Parkinsonism (motor symptoms similar to Parkinson's disease).",
        "vascular disease": "Refers to cognitive impairment caused by conditions that \nblock or reduce blood flow to the brain, depriving brain cells of \nvital oxygen and nutrients. This can result from strokes, transient ischemic \nattacks, or other conditions affecting the blood vessels in the brain.",
        "traumatic brain injury (TBI)": "An injury to the brain caused by an external \nforce, such as a blow to the head. TBI can result in a range of \ncognitive impairments, including difficulties with attention, memory, and executive \nfunctioning. The severity and duration of cognitive symptoms can vary widely based on the extent of the injury.",
        "substance/medication use": "Cognitive impairment resulting from the chronic \nuse of substances, including drugs and alcohol, or the use of \nmedications. The effects can persist beyond the period of intoxication or withdrawal, \nand may include memory loss, difficulty concentrating, and impaired judgment.",
        "HIV infection": "HIV can affect the brain and lead to cognitive impairment. \nThis occurs when the virus invades the central nervous system, causing \na decline in cognitive functions such as memory, attention, and executive \nfunction, often referred to as HIV-associated neurocognitive disorder (HAND).",
        "prion disease": "A group of rare, fatal brain disorders caused by prions, \nwhich are misfolded proteins that cause other proteins in the brain to misfold \nas well. This leads to rapid cognitive decline and motor dysfunction. \nCreutzfeldt-Jakob disease is the most well-known prion disease.",
        "parkinson's disease": "A progressive neurological disorder that primarily \naffects movement, but can also lead to cognitive impairment. Symptoms include \ntremors, stiffness, slowness of movement, and balance problems. Cognitive \ndecline can occur as the disease progresses, particularly affecting executive functions and memory.",
        "huntington's disease": "A hereditary neurodegenerative disorder caused by a \ngenetic mutation. It leads to the progressive breakdown of nerve cells in the \nbrain, affecting movement, cognition, and emotions. Cognitive symptoms \noften include difficulties with planning, organization, and memory.",
        "multiple etiologies": "Refers to cognitive impairment caused by more than one \ncontributing factor or condition. For example, a person may have cognitive \ndecline due to both Alzheimer's disease and cerebrovascular disease.",
        "unspecified etiology": "Used when cognitive impairment is observed, but the \nexact cause cannot be determined. This diagnosis is often provisional, pending \nfurther evaluation or testing.",

        # personality disorders (page 733- page 779):
        "cluster A personality disorders": "odd or eccentric behavior (paranoid personality \ndisorder; schizoid personality disorder; schizotypal personality disorder)",
        "cluster B personality disorders": "dramatic, emotional, or erratic behavior (e.g., antisocial \npersonality disorder; borderline personality disorder; histrionic \npersonality disorder; narcissistic personality disorder",
        "cluster C personality disorder": "anxious or fearful behavior (e.g., avoidant personality \ndisorder; dependent personality disorder; obsessive-compulsive personality disorder)",
        # cluster A personality disorders:
        "paranoid personality disorder": "A pattern of distrust and suspiciousness such that others' \nmotives are interpreted as malevolent.",
        "schizoid personality disorder": "A pattern of detachment from social relationships and a \nrestricted range of emotional expression.",
        "schizotypal personality disorder": "A pattern of acute discomfort in close relationships, \ncognitive or perceptual distortions, and eccentricities of behavior.",
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
        "personality change due to another medical condition": "A personality disturbance that is a direct pathophysiological\n consequence of another medical condition.",
        "other specified personality disorder": "Presentations where symptoms characteristic of a personality disorder cause\n significant distress or impairment but do not meet the full criteria\n for any specific personality disorder.",
        "unspecified personality disorder": "Symptoms characteristic of a personality disorder that cause clinically significant\n distress or impairment but do not meet the full criteria for any\n specific personality disorder.",

        # paraphilic disorders (page 779- page 803):
        "paraphilic disorders" : "A paraphilic disorder is a paraphilia that is currently causing distress or impairment \nto the individual or a paraphilia whose satisfaction has entailed \npersonal harm or risk of harm to others. A paraphilia is a necessary but not a sufficient condition for \nhaving a paraphilic disorder, and a paraphilia by itself does not necessarily justify or require clinical intervention",
        "voyeuristic disroder": "Over a period of at least 6 months, recurrent and intense sexual arousal from observing an\n unsuspecting person who is naked, in the process of disrobing, or\n engaging in sexual activity, as manifested by fantasies, urges, or behaviors.",
        "exhibitionist disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from the exposure\n of one’s genitals to an unsuspecting person, as manifested by\n fantasies, urges, or behaviors.",
        "frotteuristic disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from touching or\n rubbing against a nonconsenting person, as manifested by fantasies,\n urges, or behaviors.",
        "sexual masochism disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from the act\n of being humiliated, beaten, bound, or otherwise made to suffer, \nas manifested by fantasies, urges, or behaviors.",
        "sexual sadism disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from the physical\n or psychological suffering of another person, as manifested by \nfantasies, urges, or behaviors.",
        "pedophilic disorder": "Over a period of at least 6 months, recurrent, intense sexually arousing fantasies, sexual urges,\n or behaviors involving sexual activity with a prepubescent \nchild or children (generally age 13 years or younger).",
        "fetishistic disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from either the use of\n nonliving objects or a highly specific focus on nongenital body \npart(s), as manifested by fantasies, urges, or behaviors.",
        "transvestic disorder": "Over a period of at least 6 months, recurrent and intense sexual arousal from cross-dressing, as\n manifested by fantasies, urges, or behaviors.",
        "other specified paraphilic disorder": "Presentations that cause clinically significant distress or impairment in social,\n occupational, or other important areas of functioning but do \nnot meet the full criteria for any of the disorders in the paraphilic disorders diagnostic class.",
        "unspecified paraphilic disorder": "Symptoms characteristic of a paraphilic disorder that cause clinically significant\n distress or impairment in social, occupational, or other important \nareas of functioning but do not meet the full criteria for any specific paraphilic disorder.",

        # other mental disorders and additional codes (page 803 - page 807):
        "other mental disorders and additional codes" : "This chapter provides diagnostic codes for psychiatric presentations \nthat are mental disorders (i.e., symptoms cause clinically significant \ndistress or impairment in social, occupational, or other important areas of functioning) but that do not \nmeet diagnostic requirements for any of the mental disorders in the prior Section II chapters",
        "other specified mental disorder": "This category applies to presentations where symptoms characteristic of a mental \ndisorder cause clinically significant distress or impairment but do \nnot meet the full criteria for any specific mental disorder. The specific reason why the full criteria are not met is specified.",
        "unspecified mental disorder": "Used when symptoms characteristic of a mental disorder are present but there is insufficient \ninformation to determine the specific disorder, often used in \nsituations where a more specific diagnosis cannot be made.",
        "no diagnosis or condition": "This code applies when an individual has been evaluated, and it is determined that no mental \ndisorder or condition is present.",

        # medication-induced movement disorders and other adverse effects of medication (page 807 - page 821):
        "medication-induced movement disorders and other adverse effects of medication" : "Medication-Induced Movement Disorders covers side effects from medications used in mental and medical treatments, \nincluding parkinsonism, neuroleptic malignant syndrome, dystonia, and tardive dyskinesia. These disorders must be distinguished from similar mental conditions like anxiety.",
        "neuroleptic malignant syndrome (NMS)": "A life-threatening condition associated with the use of antipsychotic medications\n and other dopamine receptor-blocking agents. It is characterized by\n muscle rigidity, fever, autonomic instability, and altered mental status.",
        "medication-induced parkinsonism": "A disorder that mimics Parkinson’s disease, caused by medications, particularly antipsychotics\n and other dopamine receptor-blocking agents. Symptoms include\n tremors, bradykinesia (slowness of movement), rigidity, and postural instability.",
        "medication-induced acute dystonia": "A condition involving involuntary muscle contractions that can cause twisting and repetitive\n movements or abnormal postures. These symptoms can occur shortly\n after starting a medication.",
        "medication-induced acute akathisia": "A syndrome characterized by a subjective feeling of inner restlessness and a compelling need\n to be in constant motion. Patients may exhibit repetitive\n movements such as pacing or fidgeting.",
        "tardive dyskinesia": "A disorder characterized by repetitive, involuntary movements, particularly of the face and tongue, but also\n involving the limbs and trunk. It is a potential long-term\n side effect of antipsychotic medications.",
        "tardive dystonia": "A form of tardive dyskinesia where sustained muscle contractions cause twisting and repetitive movements\n or abnormal postures.",
        "tardive akathisia": "A variant of tardive dyskinesia that involves persistent, involuntary movements and restlessness that develops\n after long-term use of antipsychotic medications.",
        "medication-induced postural tremor": "A fine tremor occurring when the affected body part is held against gravity, such as holding\n out the arms. It can be caused by medications like lithium, valproate, and others.",
        "other medication-induced movement disorders": "This category includes movement disorders induced by medications that do not fit into\n the specific categories listed above. Examples might include\n movement disorders resembling neuroleptic malignant syndrome but caused \nby medications other than antipsychotics.",
        "antidepressant discontinuation syndrome": "A syndrome that can occur following the discontinuation or significant reduction in dosage\n of an antidepressant, particularly if the medication has been\n taken for an extended period. Symptoms can include flu-like symptoms, \ninsomnia, nausea, imbalance, sensory disturbances, and hyperarousal.",

    }

    # Prioritize specific matching
    for disorder, keywords in disorder_keywords_maps.items():
        if all(token in tokens for token in keywords):
            if disorder in disorder_descriptions_maps:
                return disorder_descriptions_maps[disorder]
            else:
                return "Sorry, I don't have information on that disorder right now."

    # If no exact matches, look for partial matches
    for disorder, keywords in disorder_keywords_maps.items():
        if any(token in tokens for token in keywords):
            if disorder in disorder_descriptions_maps:
                return disorder_descriptions_maps[disorder]
            else:
                return "Sorry, I don't have information on that disorder right now."

    # If no matches are found, ask for clarification
    return "I'm not sure how to respond to that. Could you provide more details?"

# Main Program:
while True:
    user_input = input("You: ")

    #Exit condition:
    if user_input.lower() in {"exit", "quit", "bye", "see you","I am done","goodbye", "okay, bye","yep, see ya later", "I'm done, thanks","Alright, thanks for the info"}:
        print("EVE: Goodbye! Have a great day!")
        break

    response = eve(user_input)
    print(f"EVE: {response}")