"""All ZeroUnit constants must be anthropocentric"""
# -- Layer 1: Core daily anthropocentric consumption constants -- 
# The five immutable pillars of the physical economy.
# This serves as the unchanging benchmark of global system measurements. 

ZEROUNIT_REGISTRY = {
    "LABOR":{
        "base_volume":8.0,
        "unit":"hours",
        "descriprtion":"Standard working day space-time (human kinetic energy capacity)"
        #standard daily working hours are set as human labor daily standard
    },
    #everything that burns and releases energy, that's why fuel is not in liquids or bulks
    "FUEL":{
        "base_volume":8.0,
        "unit":"L (eq)", # L or equivalent required to release 260MJ of thermal energy 
        "description": "Standard daily thermal/kinetic energy quantum (260MJ chemical/nuclear equivalent)"
    },
    "BULK":{
        "base_volume":0.45,
        "unit":"kg",
        "description": "Standard mass quantum of physical matter (eliminates specification/packaging fraud)"
    },
    "LIQUID":{
        "base_volume":0.5,
        "unit":"L",
        "description":"Standard single-use liquid volume for commercial fluids (combats shrinkflation)"
    },
    "DATA":{
        "base_volume":10.0,
        "unit":"kWh",
        "description":"Standard electrical or digital energy and computing capacity quantum (infrastructure benchmark)"
    }
}

# -- Layer 2: Thermodynamic energy dividers (fuel converters) --
# Precise physical equivalents required to release exactly 260MJ of thermal energy.
# The AI engine divides raw invoice volumes by these constants to get normalized ZU

FUEL_ENERGY_DIVIDERS = {
    #Liquid petroleum products (logistics) - measured in Liters
    "gasoline": {"unit":"L", "divider":8.0, "description": "Standard octane gasoline that necessary to release 260MJ of thermal energy"},
    "diesel": {"unit":"L", "divider":7.2, "description": "Standard diesel fuel (dense transport logistics) that necessary to release 260MJ of thermal energy"},
    "jet_fuel": {"unit":"L", "divider":7.4, "description": "Standard aviation kerosine (air freight) that necessary to release 260MJ of thermal energy"},
    "fuel_oil": {"unit":"L", "divider":6.5, "description": "Standard heavy fuel oil/Mazut (industrial/marine)"},

    #Gaseous Energy Carriers - measured in Cubic Meters or Kilograms
    "natural_gas":{"unit":"m3", "divider":7.4, "description":"Standard Natural gas / Methane (pipeline utilities) that necessary to release 260MJ of thermal energy"},
    "lpg":{"unit":"L", "divider":9.8, "description":"Standard liquified petroleum gas (Propane-Butane) that necessary to release 260MJ of thermal energy"},
    "hydrogen":{"unit":"kg", "divider":2.16, "description":"Standard standard compressed/liquid hydrogen that necessary to release 260MJ of thermal energy"},

    #Solid Combustibles (Heaby Industrial Power) - measured in Kilograms
    "hard_coal": {"unit":"kg", "divider":9.6, "description":"Standard high-grade hard coal (Anthracite) that necessary to release 260MJ of thermal energy"},
    "brown_coal": {"unit":"kg", "divider":17.3, "description":"Standard low-grade brown coal (Lignite) that necessary to release 260MJ of thermal energy"},
    "firewood": {"unit":"kg", "divider":17.4, "description":"Standard dry cordwood that necessary to release 260MJ of thermal energy"},
    "pallets": {"unit":"kg", "divider":14.8, "description":"Standard fuel pallets / Biomass briquettes that necessary to release 260MJ of thermal energy"},

    #Nuclear Power Matrix - measured in Grams
    "uranium_235": {"unit":"g", "divider":0.0031, "description":"Pure Uranium-235 isotropic fission equivalent"},


}