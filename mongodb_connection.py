from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # update URI if needed
db = client["market_reports"]
collection = db["reports"]

# 1st Report - Automotive Mirror Market
report1 = {
  "report_id": "AUTO-001",
  "title": "The Global Automotive Mirror Market",
  "author": "sanket",
  "base_year": 2024,
  "forecast_year": "2025-2030",
  "base_year_value_usd_billion": 12.8,
  "forecast_year_value_usd_billion": 17.5,
  "cagr_percent": 5.2,
  "pages": 250,
  "dispatch_status": "Immediate",
  "category": "Automotive",
  "sub_category": "Components & Systems",
  "sub_sub_category": "Mirror Systems",
  "type": "Global",

  "growth_drivers": [
    "Rising emphasis on vehicle safety regulations by global agencies.",
    "Increasing adoption of advanced driver assistance systems (ADAS).",
    "Growth in electric and autonomous vehicles requiring camera-based mirror systems.",
    "Consumer preference for luxury vehicles with integrated smart mirror technologies."
  ],

  "pitfalls": [
    "High cost of electronic and camera-based mirrors.",
    "Regulatory hurdles in mirrorless vehicle approvals.",
    "Potential durability and reliability issues in harsh conditions."
  ],

  "opportunities": [
    "Development of smart mirrors integrating display and navigation systems.",
    "Expansion in aftermarket sales in emerging economies.",
    "Integration of AI and IoT for improved driver assistance."
  ],

  "market_segmentation": {
    "by_product_type": [
      {
        "segment": "Interior Rear-view Mirrors (IRVM)",
        "description": "Traditionally used mirrors; shifting towards auto-dimming and digital display types.",
        "market_share_percent_2024": 35
      },
      {
        "segment": "Exterior Mirrors (ORVM)",
        "description": "Largest segment due to safety regulations; increasing adoption of power-adjustable and camera-integrated systems.",
        "market_share_percent_2024": 50
      },
      {
        "segment": "Smart Mirrors",
        "description": "Fastest-growing segment, featuring embedded cameras and infotainment displays.",
        "cagr_percent_2025_2030": 8.1
      }
    ],
    "by_vehicle_type": [
      "Passenger Vehicles",
      "Commercial Vehicles",
      "Electric Vehicles (EVs)"
    ],
    "by_technology": [
      "Conventional Mirrors",
      "Auto-dimming Mirrors",
      "Blind Spot Detection Mirrors",
      "Camera-based Mirrors (CMS)"
    ]
  },

  "regional_insights": [
    {
      "region": "North America",
      "market_share_percent_2024": 28,
      "key_insights": "Strong regulatory standards and adoption of ADAS."
    },
    {
      "region": "Europe",
      "market_share_percent_2024": 31,
      "key_insights": "Leading in smart and digital mirror adoption."
    },
    {
      "region": "Asia-Pacific",
      "market_share_percent_2024": 34,
      "key_insights": "Highest production and sales of vehicles."
    },
    {
      "region": "Latin America & MEA",
      "market_share_percent_2024": 7,
      "key_insights": "Growing automotive manufacturing base."
    }
  ],

  "market_leaders": [
    "Gentex Corporation",
    "Magna International Inc.",
    "Ficosa International S.A.",
    "Murakami Corporation",
    "SMR Automotive"
  ],

  "recent_developments": [
    {"year": 2024, "description": "Gentex launched a new full-display mirror with integrated camera view."},
    {"year": 2025, "description": "Magna introduced a camera-monitoring system replacing side mirrors in luxury EVs."},
    {"year": 2025, "description": "Ficosa collaborated with OEMs in Europe to integrate ADAS-enabled mirrors."}
  ],

  "future_outlook": {
    "summary": "The future of the automotive mirror market is expected to move toward digitization and integration.",
    "key_points": [
      "Transition from traditional mirrors to digital and smart solutions.",
      "Strong potential in Asia-Pacific and EV segment.",
      "Companies investing heavily in R&D and OEM partnerships."
    ]
  },

  "content": "The global automotive mirror market is witnessing steady growth, driven by increasing vehicle production, technological advancements in mirror systems, and growing demand for safety and comfort features. Automotive mirrors — including interior rear-view, exterior side-view, and smart mirrors — are essential components that enhance visibility and driver awareness.\n\nIn 2024, the global automotive mirror market was valued at approximately USD 12.8 billion and is projected to reach USD 17.5 billion by 2030, growing at a CAGR of 5.2% during the forecast period (2025–2030).\n\nKey Market Drivers:\n\nRising emphasis on vehicle safety regulations by global agencies.\nIncreasing adoption of advanced driver assistance systems (ADAS).\nGrowth in electric and autonomous vehicles requiring camera-based mirror systems.\nConsumer preference for luxury vehicles with integrated smart mirror technologies.\n\nKey Market Challenges:\n\nHigh cost of electronic and camera-based mirrors.\nRegulatory hurdles in mirrorless vehicle approvals.\nPotential durability and reliability issues in harsh conditions.\n\nMarket Opportunities:\n\nDevelopment of smart mirrors integrating display and navigation systems.\nExpansion in aftermarket sales in emerging economies.\nIntegration of AI and IoT for improved driver assistance.\n\nMarket Segmentation and Trends\n\nBy Product Type:\n\n1. Interior Rear-view Mirrors (IRVM): Traditionally used mirrors; shifting towards auto-dimming and digital display types. Market share (2024): 35%.\n2. Exterior Mirrors (ORVM): Largest segment due to safety regulations; increasing adoption of power-adjustable and camera-integrated systems. Market share (2024): 50%.\n3. Smart Mirrors: Fastest-growing segment, featuring embedded cameras and infotainment displays. Expected CAGR (2025–2030): 8.1%.\n\nBy Vehicle Type:\n\nPassenger Vehicles: Dominant segment, driven by consumer demand for advanced safety and comfort features.\nCommercial Vehicles: Growing adoption of durable and wide-angle mirrors for logistics and heavy vehicles.\nElectric Vehicles (EVs): Emerging category integrating digital mirrors for aerodynamic efficiency.\n\nBy Technology:\n\nConventional Mirrors\nAuto-dimming Mirrors\nBlind Spot Detection Mirrors\nCamera-based Mirrors (CMS)\n\nThe camera-based mirror system (CMS) segment is anticipated to expand rapidly, supported by regulatory approval in markets such as Japan and Europe.\n\nBy Region:\n\nRegion\t2024 Market Share\tKey Insights\nNorth America\t28%\tStrong regulatory standards and adoption of ADAS.\nEurope\t31%\tLeading in smart and digital mirror adoption.\nAsia-Pacific\t34%\tHighest production and sales of vehicles.\nLatin America & MEA\t7%\tGrowing automotive manufacturing base.\n\nCompetitive Landscape & Future Outlook\n\nKey Market Players:\n1. Gentex Corporation – Leader in auto-dimming and smart mirror technologies.\n2. Magna International Inc. – Strong OEM partnerships; innovating camera-based mirror systems.\n3. Ficosa International S.A. – Focused on intelligent mirror systems integrated with sensors.\n4. Murakami Corporation – Key supplier for Japanese automakers.\n5. SMR Automotive – Specializes in high-end exterior mirror assemblies.\n\nRecent Developments:\n2024: Gentex launched a new full-display mirror with integrated camera view.\n2025: Magna introduced a camera-monitoring system replacing side mirrors in luxury EVs.\n2025: Ficosa collaborated with OEMs in Europe to integrate ADAS-enabled mirrors.\n\nFuture Outlook:\n\nThe future of the automotive mirror market is expected to move toward digitization and integration. Camera-based systems and AI-assisted driver monitoring will become standard in mid- to high-range vehicles. Moreover, as regulations evolve, mirrorless vehicles may enter mainstream production within the next 5–7 years.\n\nKey Takeaways:\n\nMarket projected to grow steadily through 2030.\nTransition from traditional mirrors to digital and smart solutions.\nStrong potential in Asia-Pacific and EV segment.\nCompanies investing heavily in R&D and OEM partnerships."
}


# 2nd Report - Sodium-Potassium Market
report2 = {
  "report_id": "CHEM-001",
  "title": "Global Sodium-Potassium Market",
  "author": "Aniket",
  "base_year": 2024,
  "forecast_year": "2025-2030",
  "base_year_value_usd_million": 620,
  "forecast_year_value_usd_million": 910,
  "cagr_percent": 6.5,
  "pages": 220,
  "dispatch_status": "Immediate",
  "category": "Chemical and Materials",
  "sub_category": "Metals and Alloys",
  "sub_sub_category": "Sodium-Potassium Alloys",
  "type": "Global",

  "growth_drivers": [
    "Rising demand for efficient heat transfer fluids in power generation and nuclear industries.",
    "Increasing adoption of sodium-potassium batteries for renewable energy storage.",
    "Growth in metal processing and catalyst applications.",
    "Expansion of chemical manufacturing and laboratory research sectors."
  ],

  "pitfalls": [
    "High reactivity and handling risk of sodium-potassium alloy.",
    "Strict environmental and safety regulations for storage and transportation.",
    "Limited availability of specialized containment materials."
  ],

  "opportunities": [
    "Development of advanced NaK-based energy storage systems.",
    "Application in space exploration and nuclear fusion research.",
    "Increasing research investment in alkali metal-based coolants."
  ],

  "market_segmentation": {
    "by_form": [
      {
        "segment": "Liquid Sodium-Potassium Alloy (NaK)",
        "description": "Most common form; used as coolant and heat transfer medium in nuclear reactors and solar plants.",
        "market_share_percent_2024": 72
      },
      {
        "segment": "Solid Sodium-Potassium Compounds",
        "description": "Utilized in specific chemical syntheses and catalyst preparations.",
        "market_share_percent_2024": 28
      }
    ],
    "by_application": [
      "Heat Transfer Fluid",
      "Energy Storage Systems",
      "Chemical Synthesis",
      "Metal Processing",
      "Research & Development"
    ],
    "by_end_use_industry": [
      {"industry": "Energy & Power", "market_share_percent_2024": 38, "insight": "Demand from thermal and nuclear plants."},
      {"industry": "Chemicals", "market_share_percent_2024": 27, "insight": "Use in synthesis and catalytic reactions."},
      {"industry": "Electronics", "market_share_percent_2024": 15, "insight": "Emerging use in battery technology."},
      {"industry": "Aerospace & Defense", "market_share_percent_2024": 12, "insight": "Application in space propulsion and cooling."},
      {"industry": "Others (Research, Labs)", "market_share_percent_2024": 8, "insight": "Academic and industrial research usage."}
    ]
  },

  "regional_insights": [
    {"region": "North America", "market_share_percent_2024": 30, "key_insights": "Strong R&D base and nuclear applications."},
    {"region": "Europe", "market_share_percent_2024": 26, "key_insights": "Emphasis on renewable energy integration."},
    {"region": "Asia-Pacific", "market_share_percent_2024": 35, "key_insights": "Fastest-growing region with industrial expansion."},
    {"region": "Latin America & MEA", "market_share_percent_2024": 9, "key_insights": "Gradual industrial adoption and investments."}
  ],

  "market_leaders": [
    "Merck KGaA",
    "Thermo Fisher Scientific Inc.",
    "American Elements",
    "Sigma-Aldrich (MilliporeSigma)",
    "Alfa Aesar (Thermo Fisher Brand)"
  ],

  "recent_developments": [
    {"year": 2024, "description": "Merck introduced enhanced containment solutions for alkali metal storage."},
    {"year": 2025, "description": "American Elements announced pilot production of NaK-based energy storage fluids."},
    {"year": 2025, "description": "Collaboration between Thermo Fisher and European energy firms for heat transfer system trials using NaK."}
  ],

  "future_outlook": {
    "summary": "The sodium-potassium market is expected to advance steadily with the rise of clean energy technologies and energy storage innovation.",
    "key_points": [
      "Rising adoption in renewable energy and battery storage sectors.",
      "Asia-Pacific to lead in production and industrial usage.",
      "Ongoing R&D to enhance safety and material stability of NaK alloys."
    ]
  },

  "content": "The global sodium-potassium market is experiencing moderate growth, supported by increasing industrial applications, demand from energy storage systems, and its use in specialized chemical and metallurgical processes. Sodium-potassium (NaK) alloys are primarily used as heat transfer agents, reducing agents, and coolant materials in various industrial and laboratory settings.\n\nIn 2024, the global sodium-potassium market was valued at USD 620 million, and it is projected to reach USD 910 million by 2030, growing at a CAGR of 6.5% during the forecast period (2025–2030).\n\nKey Market Drivers:\nRising demand for efficient heat transfer fluids in power generation and nuclear industries.\nIncreasing adoption of sodium-potassium batteries for renewable energy storage.\nGrowth in metal processing and catalyst applications.\nExpansion of chemical manufacturing and laboratory research sectors.\n\nKey Market Challenges:\nHigh reactivity and handling risk of sodium-potassium alloy.\nStrict environmental and safety regulations for storage and transportation.\nLimited availability of specialized containment materials.\n\nMarket Opportunities:\nDevelopment of advanced NaK-based energy storage systems.\nApplication in space exploration and nuclear fusion research.\nIncreasing research investment in alkali metal-based coolants.\n\nMarket Segmentation and Trends\n\nBy Form:\n1. Liquid Sodium-Potassium Alloy (NaK): Most common form; used as coolant and heat transfer medium in nuclear reactors and solar plants. Market share (2024): 72%.\n2. Solid Sodium-Potassium Compounds: Utilized in specific chemical syntheses and catalyst preparations. Market share (2024): 28%.\n\nBy Application:\nHeat Transfer Fluid: Widely used in nuclear and solar thermal power plants for efficient heat exchange.\nEnergy Storage Systems: Sodium-potassium alloys are gaining attention in next-generation Na-ion and NaK batteries.\nChemical Synthesis: Acts as a reducing agent and catalyst in organic and inorganic reactions.\nMetal Processing: Used in removing oxygen and other impurities from metals.\nResearch & Development: Key material in laboratories and space technology research.\n\nBy End-Use Industry:\nEnergy & Power: 38% - Demand from thermal and nuclear plants.\nChemicals: 27% - Use in synthesis and catalytic reactions.\nElectronics: 15% - Emerging use in battery technology.\nAerospace & Defense: 12% - Application in space propulsion and cooling.\nOthers (Research, Labs): 8% - Academic and industrial research usage.\n\nBy Region:\nNorth America: 30% - Strong R&D base and nuclear applications.\nEurope: 26% - Emphasis on renewable energy integration.\nAsia-Pacific: 35% - Fastest-growing region with industrial expansion.\nLatin America & MEA: 9% - Gradual industrial adoption and investments.\n\nCompetitive Landscape & Future Outlook\nKey Market Players:\n1. Merck KGaA – Major supplier of sodium-potassium reagents and laboratory chemicals.\n2. Thermo Fisher Scientific Inc. – Offers high-purity NaK compounds for research and industrial applications.\n3. American Elements – Focused on production of specialty alloys and metallic materials.\n4. Sigma-Aldrich (MilliporeSigma) – Provides custom sodium-potassium products for R&D use.\n5. Alfa Aesar (Thermo Fisher Brand) – Supplies laboratory-grade NaK alloys worldwide.\n\nRecent Developments:\n2024: Merck introduced enhanced containment solutions for alkali metal storage.\n2025: American Elements announced pilot production of NaK-based energy storage fluids.\n2025: Collaboration between Thermo Fisher and European energy firms for heat transfer system trials using NaK.\n\nFuture Outlook:\nThe sodium-potassium market is expected to advance steadily with the rise of clean energy technologies and energy storage innovation. Research in sodium-based batteries and next-gen cooling systems for space and nuclear applications will drive demand. However, strict handling standards and environmental safety will remain major considerations.\n\nKey Takeaways:\nMarket projected to reach USD 910 million by 2030.\nRising adoption in renewable energy and battery storage sectors.\nAsia-Pacific to lead in production and industrial usage.\nOngoing R&D to enhance safety and material stability of NaK alloys."
}


# 3rd Report - India Animal Veterinary Market
report3 = {
  "report_id": "HEALTH-001",
  "title": "India Animal Veterinary Market",
  "author": "Aditya",
  "base_year": 2024,
  "forecast_year": "2025-2030",
  "base_year_value_usd_billion": 2.0,
  "forecast_year_value_usd_billion": 3.6,
  "cagr_percent": 9.2,
  "pages": 230,
  "dispatch_status": "Immediate",
  "category": "Healthcare",
  "sub_category": "Animal Health & Veterinary",
  "sub_sub_category": "Veterinary Pharmaceuticals & Services",
  "type": "Country",

  "growth_drivers": [
    "Rising number of pet adoptions in urban areas and growing trend of pet humanization.",
    "Expansion of livestock farming and dairy production across rural India.",
    "Increasing government programs for vaccination and zoonotic disease control.",
    "Technological advancements in veterinary diagnostics, telemedicine, and wearables."
  ],

  "pitfalls": [
    "Limited access to veterinary services in rural regions.",
    "Shortage of trained veterinarians and specialists.",
    "Price sensitivity among small livestock farmers.",
    "Regulatory delays in the approval of new veterinary drugs and vaccines."
  ],

  "opportunities": [
    "Growing adoption of pet insurance and preventive healthcare.",
    "Expansion of online veterinary pharmacies and tele-vet platforms.",
    "Increasing investments in vaccine production and diagnostic R&D.",
    "Public-private collaborations to improve livestock disease management."
  ],

  "market_segmentation": {
    "by_product_type": [
      {"segment": "Veterinary Pharmaceuticals", "description": "Dominant segment, including antibiotics, antiparasitics, and anti-inflammatory drugs. High demand across both companion and livestock sectors.", "market_share_percent_2024": 44},
      {"segment": "Vaccines", "description": "Rapidly growing due to government immunization drives for cattle and poultry, and preventive care awareness among pet owners.", "market_share_percent_2024": 27},
      {"segment": "Diagnostics", "description": "Fastest-growing category with the rise of molecular testing, imaging, and portable diagnostic kits in urban and rural clinics.", "cagr_percent_2025_2030": 10.5},
      {"segment": "Veterinary Equipment & Consumables", "description": "Includes surgical instruments, monitoring tools, and devices for farm animal management.", "market_share_percent_2024": 16},
      {"segment": "Veterinary Services", "description": "Covers clinics, telemedicine, grooming, and emergency care. Expanding rapidly in Tier-1 and Tier-2 cities.", "market_share_percent_2024": 13}
    ],
    "by_animal_type": [
      "Companion Animals (Dogs, Cats, Horses)",
      "Livestock (Cattle, Poultry, Swine, Sheep)",
      "Aquatic & Exotic Animals"
    ],
    "by_end_user": [
      {"industry": "Veterinary Clinics & Hospitals", "market_share_percent_2024": 42, "insight": "Core service providers in cities; increasing adoption of advanced diagnostics."},
      {"industry": "Livestock Farms", "market_share_percent_2024": 30, "insight": "High vaccine and medicine consumption for dairy and poultry."},
      {"industry": "Research & Academic Institutes", "market_share_percent_2024": 15, "insight": "Focus on vaccine R&D and disease control studies."},
      {"industry": "Others (Tele-vet & Online Platforms)", "market_share_percent_2024": 13, "insight": "Fastest-growing channel, especially post-pandemic."}
    ]
  },

  "regional_insights": [
    {"region": "North India", "market_share_percent_2024": 28, "key_insights": "High dairy farming activity and government programs."},
    {"region": "South India", "market_share_percent_2024": 27, "key_insights": "Growing pet ownership and livestock care facilities."},
    {"region": "West India", "market_share_percent_2024": 25, "key_insights": "Presence of major veterinary pharma manufacturing units."},
    {"region": "East India", "market_share_percent_2024": 20, "key_insights": "Rising poultry and aquaculture production."}
  ],

  "market_leaders": [
    "Indian Immunologicals Ltd (IIL)",
    "Hester Biosciences Ltd",
    "Zoetis India",
    "Boehringer Ingelheim Animal Health India",
    "Elanco India",
    "Virbac India"
  ],

  "recent_developments": [
    {"year": 2024, "description": "Indian Immunologicals launched a new foot-and-mouth disease (FMD) vaccine under government partnership."},
    {"year": 2025, "description": "Hester Biosciences established a new vaccine R&D center in Gujarat."},
    {"year": 2025, "description": "Zoetis India introduced AI-based diagnostic solutions for pet clinics."},
    {"year": 2025, "description": "Startups in Tier-2 cities expanded tele-vet and home care services for companion animals."}
  ],

  "future_outlook": {
    "summary": "The India animal veterinary market is expected to continue its strong growth trajectory, driven by rising demand for animal protein, growing pet care expenditure, and digital transformation in veterinary services.",
    "key_points": [
      "Market projected to reach USD 3.6 billion by 2030, growing at 9.2% CAGR.",
      "Strong growth in pet healthcare, vaccines, and diagnostics segments.",
      "South and West India to emerge as key regional markets.",
      "Increasing integration of technology, preventive care, and e-commerce shaping the future of animal health in India."
    ]
  },

  "content": "The India animal veterinary market is witnessing robust growth, supported by rising pet ownership, increasing livestock population, growing awareness about animal health, and government initiatives for disease prevention. The market encompasses veterinary pharmaceuticals, vaccines, diagnostics, equipment, and services used for both companion and livestock animals.\n\nIn 2024, the India animal veterinary market was valued at USD 2.0 billion and is projected to reach USD 3.6 billion by 2030, growing at a CAGR of 9.2% during the forecast period (2025–2030).\n\nKey Market Drivers:\nRising number of pet adoptions in urban areas and growing trend of pet humanization.\nExpansion of livestock farming and dairy production across rural India.\nIncreasing government programs for vaccination and zoonotic disease control.\nTechnological advancements in veterinary diagnostics, telemedicine, and wearables.\n\nKey Market Challenges:\nLimited access to veterinary services in rural regions.\nShortage of trained veterinarians and specialists.\nPrice sensitivity among small livestock farmers.\nRegulatory delays in the approval of new veterinary drugs and vaccines.\n\nMarket Opportunities:\nGrowing adoption of pet insurance and preventive healthcare.\nExpansion of online veterinary pharmacies and tele-vet platforms.\nIncreasing investments in vaccine production and diagnostic R&D.\nPublic-private collaborations to improve livestock disease management.\n\nMarket Segmentation and Trends\n\nBy Product Type:\n1. Veterinary Pharmaceuticals: Dominant segment, including antibiotics, antiparasitics, and anti-inflammatory drugs. High demand across both companion and livestock sectors. Market share (2024): 44%.\n2. Vaccines: Rapidly growing due to government immunization drives for cattle and poultry, and preventive care awareness among pet owners. Market share (2024): 27%.\n3. Diagnostics: Fastest-growing category with the rise of molecular testing, imaging, and portable diagnostic kits in urban and rural clinics. Expected CAGR (2025–2030): 10.5%.\n4. Veterinary Equipment & Consumables: Includes surgical instruments, monitoring tools, and devices for farm animal management. Market share (2024): 16%.\n5. Veterinary Services: Covers clinics, telemedicine, grooming, and emergency care. Expanding rapidly in Tier-1 and Tier-2 cities. Market share (2024): 13%.\n\nBy Animal Type:\nCompanion Animals (Dogs, Cats, Horses): Strongest growth segment due to increasing pet population (over 30 million pet dogs in India) and growing expenditure on pet wellness.\nLivestock (Cattle, Poultry, Swine, Sheep): Major revenue contributor owing to India’s large dairy and poultry industries and demand for vaccines and feed supplements.\nAquatic & Exotic Animals: Emerging segment due to expansion of aquaculture and exotic pet ownership.\n\nBy End-User:\nVeterinary Clinics & Hospitals: 42% - Core service providers in cities; increasing adoption of advanced diagnostics.\nLivestock Farms: 30% - High vaccine and medicine consumption for dairy and poultry.\nResearch & Academic Institutes: 15% - Focus on vaccine R&D and disease control studies.\nOthers (Tele-vet & Online Platforms): 13% - Fastest-growing channel, especially post-pandemic.\n\nBy Region:\nNorth India: 28% - High dairy farming activity and government programs.\nSouth India: 27% - Growing pet ownership and livestock care facilities.\nWest India: 25% - Presence of major veterinary pharma manufacturing units.\nEast India: 20% - Rising poultry and aquaculture production.\n\nCompetitive Landscape & Future Outlook\nKey Market Players:\n1. Indian Immunologicals Ltd (IIL) – Leading domestic producer of veterinary vaccines.\n2. Hester Biosciences Ltd – Focused on livestock vaccines and exports.\n3. Zoetis India – Strong presence in companion animal pharmaceuticals.\n4. Boehringer Ingelheim Animal Health India – Expanding portfolio in preventive care and parasitic control.\n5. Elanco India – Specialized in both livestock and pet health products.\n6. Virbac India – Known for dermatology and nutritional veterinary products.\n\nRecent Developments:\n2024: Indian Immunologicals launched a new foot-and-mouth disease (FMD) vaccine under government partnership.\n2025: Hester Biosciences established a new vaccine R&D center in Gujarat.\n2025: Zoetis India introduced AI-based diagnostic solutions for pet clinics.\n2025: Startups in Tier-2 cities expanded tele-vet and home care services for companion animals.\n\nFuture Outlook:\nThe India animal veterinary market is expected to continue its strong growth trajectory, driven by rising demand for animal protein, growing pet care expenditure, and digital transformation in veterinary services. Government initiatives like the National Animal Disease Control Programme (NADCP) and the rise of organized veterinary healthcare chains will further support market expansion.\n\nKey Takeaways:\nMarket projected to reach USD 3.6 billion by 2030, growing at 9.2% CAGR.\nStrong growth in pet healthcare, vaccines, and diagnostics segments.\nSouth and West India to emerge as key regional markets.\nIncreasing integration of technology, preventive care, and e-commerce shaping the future of animal health in India."
}


# Insert all reports
collection.insert_many([report1, report2, report3])

print("All 3 reports inserted successfully!")





