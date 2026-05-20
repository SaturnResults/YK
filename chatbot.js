/* ============================================================
   YK Assistant — Site Chatbot
   ============================================================ */
(function () {
  'use strict';

  var FRESHA = 'https://www.fresha.com/a/yk-wellness-london-westway-sports-fitness-centre-uk-1-crowthorne-road-git4ohyh';
  var WA     = 'https://api.whatsapp.com/send/?phone=%2B447910007933&text=Hi%2C+I+have+a+question+about+YK+Wellness';
  var MAPS   = 'https://maps.google.com/?q=Westway+Sports+Centre+1+Crowthorne+Road+London+W10+6RP';

  /* ── Treatments ─────────────────────────────────────────── */
  var T = {
    deepTissue: {
      name: 'Deep Tissue Massage',
      tag:  'Best for tension & pain',
      desc: 'Works into the deeper muscle layers to relieve chronic tension, reduce pain and restore full movement. From £75 for 60 minutes.',
      path: '/deep-tissue-massage-west-london/',
      icon: '💆'
    },
    sports: {
      name: 'Sports Massage',
      tag:  'Best for performance & recovery',
      desc: 'Advanced techniques for active people — accelerate recovery, prevent injury and optimise performance. From £53 for 30 minutes.',
      path: '/sports-massage-west-london/',
      icon: '🏃'
    },
    swedish: {
      name: 'Swedish Massage',
      tag:  'Best for relaxation',
      desc: 'Long, flowing strokes that improve circulation and melt away stress. Ideal for full-body relaxation. From £75 for 60 minutes.',
      path: '/swedish-massage/',
      icon: '🛁'
    },
    cbd: {
      name: 'CBD Massage',
      tag:  'Anti-inflammatory relief',
      desc: 'CBD oil combined with therapeutic massage for enhanced anti-inflammatory relief and deep relaxation. From £75 for 60 minutes.',
      path: '/cbd-massage/',
      icon: '🌿'
    },
    lymphatic: {
      name: 'Lymphatic Drainage',
      tag:  'Gentle & restorative',
      desc: 'Rhythmic massage to stimulate the lymphatic system, reduce swelling and support immunity. From £75 for 60 minutes.',
      path: '/lymphatic-drainage-massage/',
      icon: '💧'
    },
    osteopathy: {
      name: 'Osteopathy',
      tag:  'Best for structural care',
      desc: 'A hands-on approach that addresses the root cause of pain and dysfunction — not just the symptom.',
      path: '/osteopathy-services/',
      icon: '🦴'
    },
    cupping: {
      name: 'Cupping Therapy',
      tag:  'Specialised treatment',
      desc: 'Ancient therapy using suction cups to improve blood flow, relieve pain and release deep muscle tension. £75 for 60 minutes.',
      path: '/specialised-treatments/',
      icon: '🫧'
    },
    antiCellulite: {
      name: 'Anti-Cellulite Massage',
      tag:  'Specialised treatment',
      desc: 'Targets cellulite by improving lymphatic drainage and circulation for healthier skin. £75 for 60 minutes.',
      path: '/anti-cellulite-massage/',
      icon: '✨'
    },
    seniorTherapist: {
      name: 'Massage with Senior Therapist',
      tag:  'Premium experience',
      desc: 'A bespoke session with our most experienced therapist — personalised, intuitive, and deeply effective.',
      path: '/massage-with-senior-therapist/',
      icon: '⭐'
    }
  };

  /* ── Word-aware matching ─────────────────────────────────── */
  function hits(lower, keys) {
    return keys.some(function (k) {
      try {
        var escaped = k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        return new RegExp('(?:^|\\s|[^a-z])' + escaped + '(?:$|\\s|[^a-z])', 'i').test(lower);
      } catch (e) {
        return lower.indexOf(k) !== -1;
      }
    });
  }

  /* ── Intent definitions ─────────────────────────────────── */
  var INTENTS = [
    /* Greeting */
    {
      keys: ['hello', 'hi', 'hey', 'morning', 'afternoon', 'evening', 'howdy', 'hiya', 'good day', 'sup', 'yo'],
      reply: {
        text: "Hello! I'm YK Assistant. I can help you find the right treatment, answer questions about the clinic, or get you booked in.",
        chips: ['Find my treatment', 'Book now', 'Our location', 'Pricing']
      }
    },
    /* Treatment finder */
    {
      keys: ['find my treatment', 'which treatment', 'what treatment', 'help me choose', 'recommend', 'not sure what', 'what should i', 'what do i need', 'what would you suggest', 'best treatment', 'right treatment'],
      reply: {
        text: "Let's find the right treatment for you. What's your main goal?",
        chips: ['Relieve pain or aches', 'Reduce stress & relax', 'Sports recovery', 'Muscle tension', 'Not sure']
      }
    },
    /* Pain entry */
    {
      keys: ['relieve pain', 'pain or aches', 'i have pain', 'pain relief', 'i am in pain', 'aching', 'aches'],
      reply: {
        text: 'Where is the pain mainly located?',
        chips: ['Lower back', 'Neck & shoulders', 'Legs & hips', 'Spine / whole back', 'General / all over']
      }
    },
    /* Lower back */
    {
      keys: ['lower back', 'lower back pain', 'back pain', 'lumbar'],
      reply: {
        text: 'For lower back pain we typically recommend Deep Tissue Massage for muscle-related tension, or Osteopathy if the issue is more structural.',
        cards: ['deepTissue', 'osteopathy']
      }
    },
    /* Neck & shoulders */
    {
      keys: ['neck', 'shoulder', 'neck & shoulder', 'neck and shoulder', 'tight neck', 'stiff neck', 'shoulder pain'],
      reply: {
        text: 'Neck and shoulder tension responds very well to Deep Tissue Massage — it works directly on the muscles responsible.',
        cards: ['deepTissue']
      }
    },
    /* Legs & hips */
    {
      keys: ['legs', 'hips', 'legs & hips', 'legs and hips', 'leg pain', 'hip pain', 'hamstring', 'calf', 'thigh', 'glute'],
      reply: {
        text: 'For leg and hip discomfort, Deep Tissue or Sports Massage work best depending on how active you are.',
        cards: ['deepTissue', 'sports']
      }
    },
    /* Spine */
    {
      keys: ['spine', 'whole back', 'spine / whole back', 'spinal', 'sciatic', 'sciatica', 'disc', 'pinched nerve'],
      reply: {
        text: 'Spinal and whole-back issues respond best to Osteopathy — addressing root causes rather than just the symptom.',
        cards: ['osteopathy', 'deepTissue']
      }
    },
    /* General pain */
    {
      keys: ['general', 'all over', 'everywhere', 'general / all over', 'whole body'],
      reply: {
        text: 'For widespread tension or aches, Deep Tissue Massage is the most effective starting point.',
        cards: ['deepTissue']
      }
    },
    /* Relax */
    {
      keys: ['relax', 'relaxation', 'reduce stress', 'stress & relax', 'unwind', 'stress', 'anxiety', 'anxious', 'sleep', 'calm', 'burnout', 'exhausted', 'wind down', 'de-stress'],
      reply: {
        text: 'Swedish Massage is ideal — long, flowing strokes that genuinely melt away stress. A great first-time treatment too.',
        cards: ['swedish']
      }
    },
    /* Sports */
    {
      keys: ['sports recovery', 'sports massage', 'recovery', 'training', 'performance', 'athlete', 'marathon', 'running', 'gym', 'cycling', 'football', 'injury prevention', 'active', 'sporty'],
      reply: {
        text: 'Sports Massage is built for exactly this — faster recovery, injury prevention and optimised performance.',
        cards: ['sports']
      }
    },
    /* Tension */
    {
      keys: ['muscle tension', 'tension', 'tight muscles', 'stiffness', 'knots', 'tight', 'stiff', 'seized up'],
      reply: {
        text: 'Deep Tissue Massage is our most popular treatment for muscle tension — working into the deeper layers where stress accumulates.',
        cards: ['deepTissue']
      }
    },
    /* CBD */
    {
      keys: ['cbd', 'cbd massage', 'inflammation', 'anti-inflammatory', 'hemp'],
      reply: {
        text: 'Our CBD Massage combines anti-inflammatory CBD oil with therapeutic massage for enhanced relief.',
        cards: ['cbd']
      }
    },
    /* Lymphatic */
    {
      keys: ['lymphatic', 'lymph', 'drainage', 'swelling', 'immune', 'detox', 'fluid retention', 'bloating', 'lymphatic drainage'],
      reply: {
        text: 'Lymphatic Drainage is a gentle, rhythmic treatment to stimulate the lymphatic system and reduce swelling.',
        cards: ['lymphatic']
      }
    },
    /* Osteopathy */
    {
      keys: ['osteopath', 'osteopathy', 'structural', 'joint pain', 'root cause'],
      reply: {
        text: 'Osteopathy takes a whole-body approach — finding and treating the structural root cause of your pain.',
        cards: ['osteopathy']
      }
    },
    /* Cupping */
    {
      keys: ['cupping', 'cups', 'cupping therapy'],
      reply: { text: 'Cupping Therapy uses suction cups to improve blood flow, relieve pain and release deep tension. £75 for 60 minutes.', cards: ['cupping'] }
    },
    /* Anti-Cellulite */
    {
      keys: ['cellulite', 'anti-cellulite', 'anti cellulite'],
      reply: { text: 'Our Anti-Cellulite Massage targets cellulite by improving lymphatic drainage and circulation. £75 for 60 minutes.', cards: ['antiCellulite'] }
    },
    /* Senior Therapist */
    {
      keys: ['senior therapist', 'senior massage', 'experienced therapist', 'best therapist', 'most experienced'],
      reply: { text: 'Our Massage with Senior Therapist is a bespoke, premium session with our most experienced practitioner — deeply personalised and highly effective.', cards: ['seniorTherapist'] }
    },
    /* Conditions */
    {
      keys: ['conditions', 'what conditions', 'treat', 'treat conditions', 'what do you treat', 'back pain', 'neck pain', 'shoulder pain', 'sciatica', 'headache', 'anxiety', 'stress relief'],
      reply: {
        text: "We treat a wide range of conditions including back pain, neck tension, sciatica, sports injuries, stress and anxiety. See the full list on our Conditions page.",
        links: [{ text: 'Conditions We Treat →', url: '/conditions-we-treat/' }]
      }
    },
    /* Booking */
    {
      keys: ['book', 'booking', 'appointment', 'schedule', 'reserve', 'book now', 'availability', 'available slots'],
      reply: {
        text: "Book online through Fresha — view all available slots in real time and book in under two minutes.",
        links: [{ text: 'Book on Fresha →', url: FRESHA }]
      }
    },
    /* Location */
    {
      keys: ['where', 'location', 'address', 'directions', 'find you', 'our location', 'w10', 'based'],
      reply: {
        text: "We're at Westway Sports and Fitness Centre, 1 Crowthorne Road, London W10 6RP. Free parking on site.",
        links: [{ text: 'Open in Google Maps →', url: MAPS }]
      }
    },
    /* Parking */
    {
      keys: ['parking', 'park', 'car park', 'drive'],
      reply: {
        text: 'Free parking is available at Westway Sports Centre — no time limit during your appointment.'
      }
    },
    /* Transport */
    {
      keys: ['transport', 'tube', 'underground', 'bus', 'train', 'public transport', 'get there', 'travel'],
      reply: {
        text: "We're close to Latimer Road (Circle & Hammersmith & City lines) and White City (Central line). Buses 220, 295 and 316 stop nearby."
      }
    },
    /* Hours */
    {
      keys: ['open', 'opening', 'hours', 'opening hours', 'what time', 'when are you', 'close', 'closing', 'open on sunday', 'open on saturday', 'open weekends', 'open today', 'times'],
      reply: {
        text: "We're open 7 days a week:\n\nMonday – Friday: 8:00 AM – 8:00 PM\nSaturday – Sunday: 9:00 AM – 6:00 PM"
      }
    },
    /* Pricing — general */
    {
      keys: ['how much', 'price', 'pricing', 'cost', 'rates', 'charge', 'fee', 'expensive', 'cheap', 'afford'],
      reply: {
        text: 'Sessions start from £53 (30 min). Most 60-minute treatments are £75, 90 minutes are £105, and 120 minutes are £140.',
        chips: ['Swedish Massage prices', 'Deep Tissue prices', 'Sports Massage prices', 'All prices on Fresha'],
        links: [{ text: 'View all pricing →', url: FRESHA }]
      }
    },
    /* Per-treatment pricing chips */
    {
      keys: ['swedish massage prices', 'swedish massage price', 'how much is swedish', 'swedish cost'],
      reply: { text: 'Swedish Massage:\n60 min — £75\n90 min — £105\n120 min — £140', links: [{ text: 'Book →', url: FRESHA }] }
    },
    {
      keys: ['deep tissue prices', 'deep tissue price', 'how much is deep tissue', 'deep tissue cost'],
      reply: { text: 'Deep Tissue Massage:\n60 min — £75\n90 min — £105\n120 min — £140', links: [{ text: 'Book →', url: FRESHA }] }
    },
    {
      keys: ['sports massage prices', 'sports massage price', 'how much is sports', 'sports cost'],
      reply: { text: 'Sports Massage:\n30 min — £53\n60 min — £75\n90 min — £105', links: [{ text: 'Book →', url: FRESHA }] }
    },
    {
      keys: ['all prices on fresha', 'all prices', 'full price list'],
      reply: { text: 'You can see the full up-to-date price list when booking on Fresha.', links: [{ text: 'View all pricing →', url: FRESHA }] }
    },
    /* Duration */
    {
      keys: ['how long', 'duration', 'minutes', 'how long is', 'length of', 'session length'],
      reply: {
        text: 'Sessions run from 30 to 120 minutes depending on the treatment. 60 minutes is the most popular choice for a first visit.'
      }
    },
    /* Consultation */
    {
      keys: ['consultation', 'consult', 'intake', 'assessment', 'before the treatment', 'before my session'],
      reply: {
        text: 'Every session begins with a brief consultation. Your therapist will ask about your goals, any areas of concern, and health history — so the treatment is tailored specifically to you.'
      }
    },
    /* Gift cards */
    {
      keys: ['gift', 'voucher', 'gift card', 'gift voucher', 'present', 'someone else', 'buy as a gift'],
      reply: {
        text: 'Gift cards are available through Fresha — a great gift for anyone who could do with some proper rest.',
        links: [{ text: 'Buy a gift card →', url: FRESHA }]
      }
    },
    /* Reviews */
    {
      keys: ['review', 'rating', 'rated', 'stars', 'reputation', 'trusted', 'best in'],
      reply: {
        text: 'We have 400+ five-star reviews on Fresha and 140+ on Google — one of West London\'s highest-rated clinics.'
      }
    },
    /* First time */
    {
      keys: ['first time', 'first visit', 'first massage', 'new client', 'never had', 'never been', 'what to expect', 'what happens', 'nervous', 'first session'],
      reply: {
        text: 'Every session starts with a brief consultation so your therapist can understand your needs and tailor the treatment. Wear comfortable clothing — we\'ll handle everything else.'
      }
    },
    /* Contact */
    {
      keys: ['contact', 'speak to', 'talk to', 'phone', 'email', 'call', 'get in touch', 'speak to someone', 'human', 'person'],
      reply: {
        text: 'You can reach us on WhatsApp or by email at hello@ykwellness.co.uk.',
        links: [{ text: 'WhatsApp us →', url: WA }]
      }
    },
    /* Not sure / general wellbeing */
    {
      keys: ['not sure', 'unsure', 'no idea', 'general health', 'general wellbeing', 'wellbeing', 'wellness', 'maintenance'],
      reply: {
        text: "No problem — tell me a little about how you're feeling and I'll point you in the right direction.",
        chips: ['I have pain or tension', 'I want to relax', 'I\'m active / sporty', 'General wellbeing']
      }
    },
    /* Convenience chips */
    { keys: ['i have pain or tension', 'i have pain'],
      reply: { text: 'Where is it mainly?', chips: ['Lower back', 'Neck & shoulders', 'Legs & hips', 'General / all over'] }
    },
    { keys: ["i'm active / sporty", 'i\'m active', 'im active', 'i am active'],
      reply: { text: 'Sports Massage is designed for active people — keeping your body performing and recovering at its best.', cards: ['sports'] }
    },
    { keys: ['i want to relax', 'want to relax'],
      reply: { text: 'Swedish Massage is perfect for this — long, flowing strokes designed for genuine rest and relaxation.', cards: ['swedish'] }
    },
    { keys: ['general wellbeing', 'general health'],
      reply: { text: 'For ongoing wellness and maintenance, Swedish Massage is a great regular treatment — many clients combine it with Deep Tissue for specific areas.', cards: ['swedish', 'deepTissue'] }
    },
    /* Thank you */
    {
      keys: ['thank', 'thanks', 'cheers', 'great', 'helpful', 'perfect', 'brilliant', 'awesome', 'amazing', 'wonderful', 'lovely'],
      reply: {
        text: 'Happy to help! Is there anything else I can assist with?',
        chips: ['Book now', 'Our location', 'Find my treatment']
      }
    },

    /* Availability / when / space */
    {
      keys: ['when do you have space', 'when are you free', 'when can i come', 'do you have space', 'any availability', 'any slots', 'available this week', 'available today', 'available tomorrow', 'available this weekend', 'available saturday', 'available sunday', 'next available', 'earliest', 'soonest', 'free slot', 'free slots', 'when can i book', 'can i come', 'any appointments', 'when do you have', 'do you have anything', 'got any space', 'got space'],
      reply: {
        text: 'The easiest way to check availability is on Fresha — you can see all live slots in real time and book instantly.',
        links: [{ text: 'Check availability on Fresha →', url: FRESHA }]
      }
    },

    /* Cancellation policy */
    {
      keys: ['cancel', 'cancellation', 'reschedule', 'rearrange', 'change my appointment', 'change booking', 'move my appointment', 'refund', 'late cancellation', 'cancellation policy', 'cancel my booking', 'cancel appointment'],
      reply: {
        text: 'We ask for at least 24 hours’ notice to cancel or reschedule. Late cancellations may incur a charge. To cancel or move your appointment, please message us on WhatsApp.',
        links: [{ text: 'Message us on WhatsApp →', url: WA }]
      }
    },

    /* Pregnancy massage */
    {
      keys: ['pregnant', 'pregnancy', 'pregnancy massage', 'prenatal', 'ante-natal', 'antenatal', 'expecting', 'baby', 'maternity massage'],
      reply: {
        text: 'We offer specialist pregnancy massage, which is safe from the second trimester onwards. Please mention you’re pregnant when booking so we can prepare accordingly.',
        links: [{ text: 'Book on Fresha →', url: FRESHA }]
      }
    },

    /* How many sessions */
    {
      keys: ['how many sessions', 'how many treatments', 'how often', 'how regular', 'frequency', 'once a week', 'once a month', 'series of treatments', 'course of treatment', 'do i need more than one', 'do i need multiple'],
      reply: {
        text: 'It depends on your goals. For a specific injury or chronic tension, most clients see meaningful improvement after 3–4 sessions. For general maintenance and stress relief, once or twice a month is ideal.'
      }
    },

    /* What to wear / prepare */
    {
      keys: ['what to wear', 'what should i wear', 'what do i wear', 'what should i bring', 'how to prepare', 'what happens when i arrive', 'what do i need to do', 'do i need to undress', 'do i need to take clothes off', 'do i get undressed', 'naked', 'modesty', 'towel', 'draping'],
      reply: {
        text: 'Wear loose, comfortable clothing for your journey. During the session you undress to your comfort level — you will always be fully draped with a towel and only the area being worked on is uncovered.'
      }
    },

    /* Payment */
    {
      keys: ['payment', 'pay', 'cash', 'card', 'contactless', 'how do i pay', 'how to pay', 'do you take card', 'do you accept cash', 'payment methods', 'apple pay', 'google pay', 'credit card', 'debit card'],
      reply: {
        text: 'We accept card (including contactless and Apple/Google Pay) and cash. Payment is taken after your session.'
      }
    },

    /* Insurance / receipts */
    {
      keys: ['insurance', 'claim', 'receipt', 'invoice', 'private health', 'health insurance', 'bupa', 'vitality', 'axa', 'aviva', 'medical insurance'],
      reply: {
        text: 'We can provide a receipt or invoice after your session for insurance purposes. Please message us with any specific requirements and we’ll be happy to help.',
        links: [{ text: 'Message us on WhatsApp →', url: WA }]
      }
    },

    /* Couples massage */
    {
      keys: ['couples', 'couples massage', 'two people', 'me and my partner', 'partner', 'together', 'both of us', 'dual', 'duo', 'pair', 'with a friend', 'friend', 'gift for two'],
      reply: {
        text: 'We can accommodate two people at the same time — just book two consecutive appointments with our therapists. Message us on WhatsApp if you’d like help coordinating this.',
        links: [{ text: 'Message us on WhatsApp →', url: WA }]
      }
    },

    /* Male / female therapist */
    {
      keys: ['male therapist', 'female therapist', 'woman therapist', 'man therapist', 'prefer a female', 'prefer a male', 'gender', 'therapist gender', 'who are your therapists', 'who will treat me'],
      reply: {
        text: 'We have both male and female therapists. You can request a preference when booking on Fresha, or message us directly and we’ll match you with the right person.',
        links: [{ text: 'Message us on WhatsApp →', url: WA }]
      }
    },

    /* Meet the team */
    {
      keys: ['who are you', 'your team', 'meet the team', 'therapists', 'your therapist', 'who works there', 'staff', 'practitioners', 'team'],
      reply: {
        text: 'Our team includes massage therapists and an osteopath with years of clinical experience. You can meet them all on our team page.',
        links: [{ text: 'Meet the team →', url: '/meet-the-team/' }]
      }
    },

    /* Headaches / migraines */
    {
      keys: ['headache', 'migraine', 'head pain', 'tension headache', 'head', 'temple', 'forehead'],
      reply: {
        text: 'Tension headaches often originate in the neck and upper shoulders. Deep Tissue Massage targeting the neck, shoulders and base of the skull can provide significant relief.',
        cards: ['deepTissue']
      }
    },

    /* Posture / desk / office */
    {
      keys: ['posture', 'sitting all day', 'desk job', 'office worker', 'desk work', 'hunched', 'rounded shoulders', 'forward head', 'computer', 'laptop', 'work from home', 'wfh', 'sitting too much'],
      reply: {
        text: 'Poor posture from desk work is one of the most common things we treat. Deep Tissue Massage addresses the muscle imbalances directly, while Osteopathy is excellent if there’s a structural component.',
        cards: ['deepTissue', 'osteopathy']
      }
    },

    /* Injury */
    {
      keys: ['injury', 'injured', 'pulled muscle', 'strain', 'sprain', 'torn', 'overuse', 'repetitive strain', 'rsi', 'tendon', 'tendonitis', 'rotator cuff', 'frozen shoulder', 'frozen', 'whiplash'],
      reply: {
        text: 'For injuries, Sports Massage helps with acute and recovering soft tissue injuries. If you’re unsure, Osteopathy is a great option for a full assessment and treatment plan.',
        cards: ['sports', 'osteopathy']
      }
    },

    /* Knee / foot / ankle */
    {
      keys: ['knee', 'knee pain', 'foot', 'feet', 'ankle', 'plantar', 'plantar fasciitis', 'achilles', 'shin splints', 'calf pain'],
      reply: {
        text: 'For knee, foot and ankle issues, Sports Massage is particularly effective at addressing the surrounding muscle groups and reducing tension on the joint.',
        cards: ['sports']
      }
    },

    /* Wrist / arm / elbow */
    {
      keys: ['wrist', 'arm', 'elbow', 'forearm', 'tennis elbow', 'golfers elbow', 'carpal tunnel', 'hand pain'],
      reply: {
        text: 'Arm, wrist and elbow issues often respond well to Sports Massage, especially for repetitive strain or sports-related tension. Osteopathy is also highly effective for structural or nerve-related causes.',
        cards: ['sports', 'osteopathy']
      }
    },

    /* Sciatica specifically */
    {
      keys: ['sciatic', 'sciatica', 'shooting pain down leg', 'pain down my leg', 'nerve pain', 'trapped nerve', 'herniated', 'slipped disc', 'piriformis'],
      reply: {
        text: 'Sciatica and nerve-related pain are a speciality of Osteopathy — addressing the root cause rather than masking the symptom. Deep Tissue Massage can also ease the muscular tension that contributes to it.',
        cards: ['osteopathy', 'deepTissue']
      }
    },

    /* Skin concerns */
    {
      keys: ['skin', 'skin texture', 'cellulite', 'tone', 'toning', 'body confidence', 'circulation', 'fluid', 'puffy', 'puffiness', 'bloated', 'lymph node'],
      reply: {
        text: 'For skin and body concerns, our Anti-Cellulite Massage and Lymphatic Drainage are the most targeted treatments.',
        cards: ['antiCellulite', 'lymphatic']
      }
    },

    /* Stress at work / burnout */
    {
      keys: ['stressed at work', 'work stress', 'overworked', 'worn out', 'run down', 'burnt out', 'burnout', 'mentally tired', 'mentally exhausted', 'can\'t switch off', 'mind won\'t stop', 'tense'],
      reply: {
        text: 'When stress is both mental and physical, Swedish or CBD Massage are the most effective resets — calming the nervous system and releasing stored muscle tension at the same time.',
        cards: ['swedish', 'cbd']
      }
    },

    /* Post-surgery / recovery */
    {
      keys: ['surgery', 'post surgery', 'post-surgery', 'operation', 'recovering from', 'after an operation', 'lymph after surgery', 'post op', 'post-op'],
      reply: {
        text: 'Lymphatic Drainage is ideal post-surgery to reduce swelling, support healing and speed up recovery. Please wait until you have medical clearance before booking.',
        cards: ['lymphatic']
      }
    },

    /* Disability / accessibility */
    {
      keys: ['wheelchair', 'disabled', 'disability', 'accessible', 'accessibility', 'mobility', 'limited mobility'],
      reply: {
        text: 'Westway Sports Centre is fully accessible. Please message us in advance so we can ensure everything is set up comfortably for you.',
        links: [{ text: 'Message us on WhatsApp →', url: WA }]
      }
    },

    /* Minimum age / children */
    {
      keys: ['age', 'minimum age', 'how old', 'child', 'children', 'teenager', 'teen', 'under 18', 'young person'],
      reply: {
        text: 'We treat clients aged 16 and over. Clients under 18 must have a parent or guardian present and provide written consent before treatment.'
      }
    },

    /* Health conditions / contraindications */
    {
      keys: ['is it safe', 'can i have a massage if', 'health condition', 'medical condition', 'blood pressure', 'high blood pressure', 'diabetes', 'heart condition', 'cancer', 'epilepsy', 'on medication', 'taking medication', 'contraindication'],
      reply: {
        text: 'Most people can have massage safely. If you have a medical condition, please mention it when booking so our therapist can tailor the session appropriately. When in doubt, check with your GP first.'
      }
    },

    /* Tipping */
    {
      keys: ['tip', 'tipping', 'gratuity', 'should i tip', 'do i tip'],
      reply: {
        text: 'Tips are entirely optional but always appreciated by the therapist. You can leave a cash tip after your session if you’d like to.'
      }
    },

    /* Goodbye */
    {
      keys: ['bye', 'goodbye', 'see you', 'see ya', 'later', 'take care', 'that\'s all'],
      reply: {
        text: 'Take care! We look forward to seeing you at YK Wellness. Book any time on Fresha.',
        links: [{ text: 'Book on Fresha →', url: FRESHA }]
      }
    },

    /* Affirmatives (follow-up yes) */
    {
      keys: ['yes', 'yeah', 'yep', 'sure', 'ok', 'okay', 'sounds good', 'go ahead', 'please', 'definitely'],
      reply: {
        text: 'Great! What would you like to know?',
        chips: ['Find my treatment', 'Book now', 'Pricing', 'Our location']
      }
    },

    /* Negative / no */
    {
      keys: ['no', 'nope', 'nah', 'not really', 'no thanks', 'nothing else'],
      reply: {
        text: 'No problem at all. We look forward to seeing you at YK Wellness!',
        links: [{ text: 'Book on Fresha →', url: FRESHA }]
      }
    }
  ];

  var FALLBACK = {
    text: "I’m not quite sure about that one — but our team will know. Message us on WhatsApp for a quick answer.",
    links: [{ text: 'Message us on WhatsApp →', url: WA }]
  };

  /* ── Respond ────────────────────────────────────────────── */
  function resolve(input) {
    var lower = input.toLowerCase().trim();
    for (var i = 0; i < INTENTS.length; i++) {
      if (hits(lower, INTENTS[i].keys)) return INTENTS[i].reply;
    }
    return FALLBACK;
  }

  /* ── Build message element ───────────────────────────────── */
  function buildMsg(role, data) {
    var isBot = role === 'bot';
    var wrap = document.createElement('div');
    wrap.className = 'ykc-msg ykc-msg--' + role;

    var inner = '';
    if (isBot) inner += '<div class="ykc-avatar">YK</div>';
    inner += '<div class="ykc-msg__content">';

    var text = (data.text || '').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    inner += '<div class="ykc-bubble">' + text + '</div>';

    if (data.cards && data.cards.length) {
      inner += '<div class="ykc-cards">';
      data.cards.forEach(function (k) {
        var t = T[k];
        inner += '<a href="' + t.path + '" class="ykc-card">' +
          '<span class="ykc-card__icon">' + t.icon + '</span>' +
          '<div class="ykc-card__body">' +
            '<div class="ykc-card__tag">' + t.tag + '</div>' +
            '<div class="ykc-card__name">' + t.name + '</div>' +
            '<div class="ykc-card__desc">' + t.desc + '</div>' +
            '<span class="ykc-card__cta">View treatment →</span>' +
          '</div>' +
        '</a>';
      });
      inner += '</div>';
    }

    if (data.links && data.links.length) {
      data.links.forEach(function (l) {
        inner += '<a href="' + l.url + '" class="ykc-link-btn" target="_blank" rel="noopener">' + l.text + '</a>';
      });
    }

    if (data.chips && data.chips.length) {
      inner += '<div class="ykc-chips">';
      data.chips.forEach(function (c) {
        inner += '<button class="ykc-chip" type="button">' + c + '</button>';
      });
      inner += '</div>';
    }

    inner += '</div>';
    wrap.innerHTML = inner;
    return wrap;
  }

  /* ── Typing indicator ─────────────────────────────────────── */
  function addTyping(container) {
    var el = document.createElement('div');
    el.className = 'ykc-msg ykc-msg--bot ykc-msg--in';
    el.innerHTML = '<div class="ykc-avatar">YK</div>' +
      '<div class="ykc-msg__content"><div class="ykc-typing"><span></span><span></span><span></span></div></div>';
    container.appendChild(el);
    container.scrollTop = container.scrollHeight;
    return el;
  }

  var API_URL = 'https://yk-chat-api.vercel.app/api/chat';

  /* ── Engine factory ───────────────────────────────────────── */
  function createEngine(container) {
    var history = []; // conversation history for AI context

    function appendMsg(role, data) {
      var el = buildMsg(role, data);
      // Remove old chips
      container.querySelectorAll('.ykc-chips').forEach(function (c) { c.remove(); });
      container.appendChild(el);
      // Bind new chips
      el.querySelectorAll('.ykc-chip').forEach(function (chip) {
        chip.addEventListener('click', function (e) {
          e.stopPropagation();
          send(chip.textContent.trim());
        });
      });
      container.scrollTop = container.scrollHeight;
      // Animate in
      requestAnimationFrame(function () { requestAnimationFrame(function () { el.classList.add('ykc-msg--in'); }); });
    }

    function send(text) {
      if (!text.trim()) return;
      appendMsg('user', { text: text });
      history.push({ role: 'user', content: text });

      var typing = addTyping(container);

      fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: history })
      })
      .then(function (res) { return res.json(); })
      .then(function (data) {
        typing.remove();
        var reply = data.reply || FALLBACK.text;
        history.push({ role: 'assistant', content: reply });
        // Render plain text reply — convert URLs to buttons
        appendMsg('bot', formatAIReply(reply));
      })
      .catch(function () {
        // API failed — fall back to keyword matching
        typing.remove();
        history.push({ role: 'assistant', content: FALLBACK.text });
        appendMsg('bot', resolve(text));
      });
    }

    function formatAIReply(text) {
      // Pull any URLs out as link buttons; render the rest as text
      var urlRegex = /(https?:\/\/[^\s]+)/g;
      var links = [];
      var clean = text.replace(urlRegex, function (url) {
        var label = url.includes('fresha') ? 'Book on Fresha →'
                  : url.includes('whatsapp') ? 'Message on WhatsApp →'
                  : url.includes('maps') ? 'Open in Google Maps →'
                  : 'Visit →';
        links.push({ text: label, url: url });
        return '';
      }).replace(/\n{2,}/g, '\n').trim();
      return { text: clean, links: links.length ? links : undefined };
    }

    function welcome(delay) {
      setTimeout(function () {
        appendMsg('bot', {
          text: "Hello! I'm YK Assistant. I can help you find the right treatment, answer questions about the clinic, or get you booked in.",
          chips: ['Find my treatment', 'Book now', 'Our location', 'Pricing']
        });
      }, delay || 400);
    }

    return { send: send, welcome: welcome };
  }

  /* ── Floating widget ─────────────────────────────────────── */
  function mountFloating() {
    // Launcher button
    var launcher = document.createElement('button');
    launcher.className = 'ykc-launcher';
    launcher.setAttribute('aria-label', 'Open YK Assistant');
    launcher.innerHTML =
      '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
        '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>' +
      '</svg>' +
      '<span class="ykc-launcher__label">YK Assistant</span>' +
      '<span class="ykc-launcher__dot" aria-hidden="true"></span>';

    // Chat window
    var win = document.createElement('div');
    win.className = 'ykc-win';
    win.setAttribute('aria-hidden', 'true');
    win.innerHTML =
      '<div class="ykc-win__header">' +
        '<div class="ykc-win__info">' +
          '<div class="ykc-avatar ykc-avatar--lg">YK</div>' +
          '<div>' +
            '<div class="ykc-win__name">YK Assistant</div>' +
            '<div class="ykc-win__status"><span class="ykc-status-dot"></span> Online now</div>' +
          '</div>' +
        '</div>' +
        '<button class="ykc-win__close" aria-label="Close chat">' +
          '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>' +
        '</button>' +
      '</div>' +
      '<div class="ykc-messages" id="ykcMessages"></div>' +
      '<div class="ykc-input-row">' +
        '<input class="ykc-input" type="text" placeholder="Ask anything…" id="ykcInput" autocomplete="off" />' +
        '<button class="ykc-send" id="ykcSend" aria-label="Send">' +
          '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>' +
        '</button>' +
      '</div>';

    document.body.appendChild(launcher);
    document.body.appendChild(win);

    var messagesEl = win.querySelector('#ykcMessages');
    var inputEl    = win.querySelector('#ykcInput');
    var sendEl     = win.querySelector('#ykcSend');
    var closeEl    = win.querySelector('.ykc-win__close');

    var isOpen   = false;
    var inited   = false;
    var engine;

    function open() {
      isOpen = true;
      win.classList.add('open');
      win.setAttribute('aria-hidden', 'false');
      launcher.classList.add('active');
      var dot = launcher.querySelector('.ykc-launcher__dot');
      if (dot) dot.remove();
      if (!inited) {
        inited = true;
        engine = createEngine(messagesEl);
        engine.welcome(300);
      }
      setTimeout(function () { inputEl.focus(); }, 320);
    }

    function close() {
      isOpen = false;
      win.classList.remove('open');
      win.setAttribute('aria-hidden', 'true');
      launcher.classList.remove('active');
    }

    function bindSend() {
      sendEl.addEventListener('click', function () {
        var val = inputEl.value.trim();
        if (!val || !engine) return;
        inputEl.value = '';
        engine.send(val);
      });
      inputEl.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendEl.click(); }
      });
    }

    launcher.addEventListener('click', function () { isOpen ? close() : open(); });
    closeEl.addEventListener('click', close);
    bindSend();

    // Close on outside click
    document.addEventListener('click', function (e) {
      if (isOpen && !win.contains(e.target) && !launcher.contains(e.target)) close();
    });

    // Hide launcher only on mobile homepage hero; show everywhere else immediately
    function updateVisibility() {
      var isHomepage = window.location.pathname === '/' || window.location.pathname === '/index.html';
      var isMobile = window.innerWidth <= 768;
      var scrolled = window.scrollY > 350;
      // Only gate on scroll when: mobile AND on the homepage
      var visible = isOpen || !(isMobile && isHomepage) || scrolled;
      launcher.classList.toggle('ykc-launcher--visible', visible);
      win.classList.toggle('ykc-win--shifted', visible);
    }
    window.addEventListener('scroll', updateVisibility, { passive: true });
    window.addEventListener('resize', updateVisibility, { passive: true });
    updateVisibility();
  }

  /* ── Full-section chat (contact page) ────────────────────── */
  function mountSection() {
    var root = document.getElementById('ykChatSection');
    if (!root) return;

    root.innerHTML =
      '<div class="ykc-section">' +
        '<div class="ykc-section__header">' +
          '<div class="ykc-avatar ykc-avatar--lg">YK</div>' +
          '<div>' +
            '<div class="ykc-win__name">YK Assistant</div>' +
            '<div class="ykc-win__status"><span class="ykc-status-dot"></span> Online now</div>' +
          '</div>' +
        '</div>' +
        '<div class="ykc-messages ykc-section__messages" id="ykcSectionMsgs"></div>' +
        '<div class="ykc-input-row ykc-section__input">' +
          '<input class="ykc-input" type="text" placeholder="Ask anything about YK Wellness…" id="ykcSectionInput" autocomplete="off" />' +
          '<button class="ykc-send" id="ykcSectionSend" aria-label="Send">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>' +
          '</button>' +
        '</div>' +
      '</div>';

    var messagesEl = root.querySelector('#ykcSectionMsgs');
    var inputEl    = root.querySelector('#ykcSectionInput');
    var sendEl     = root.querySelector('#ykcSectionSend');

    var engine = createEngine(messagesEl);
    engine.welcome(500);

    sendEl.addEventListener('click', function () {
      var val = inputEl.value.trim();
      if (!val) return;
      inputEl.value = '';
      engine.send(val);
    });
    inputEl.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendEl.click(); }
    });
  }

  /* ── Boot ────────────────────────────────────────────────── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { mountFloating(); mountSection(); });
  } else {
    mountFloating();
    mountSection();
  }

})();
