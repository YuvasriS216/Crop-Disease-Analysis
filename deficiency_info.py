def get_deficiency_info(deficiency_name):
    """
    Get detailed information about a specific nutrient deficiency
    
    Args:
        deficiency_name (str): The name of the deficiency
        
    Returns:
        dict: Information about the deficiency
    """
    deficiency_database = {
        "Healthy": {
            "name": "Healthy Plant",
            "symptoms": "- Vibrant green coloration\n- No discoloration or spots\n- Uniform leaf shape and structure\n- Good leaf turgidity",
            "causes": "- Balanced nutrient availability\n- Adequate water supply\n- Proper environmental conditions\n- Absence of pests and diseases",
            "treatment": "- Continue with regular maintenance practices\n- Monitor for early signs of stress\n- Maintain balanced fertilization program\n- Ensure proper irrigation",
            "additional_info": "Healthy wheat plants typically display uniform green coloration throughout the leaf structure. Maintaining good agricultural practices is key to preventing nutrient deficiencies."
        },
        
        "Nitrogen Deficiency": {
            "name": "Nitrogen Deficiency",
            "symptoms": "- Yellowing (chlorosis) of older leaves, starting at the tips\n- Stunted growth\n- Pale green to yellow overall appearance\n- V-shaped yellowing pattern on leaves\n- Thin stems and reduced tillering",
            "causes": "- Insufficient nitrogen in soil\n- Leaching due to heavy rainfall\n- Low organic matter in soil\n- Inadequate fertilization\n- Waterlogged soils",
            "treatment": "- Apply nitrogen-rich fertilizers (ammonium nitrate, urea)\n- Incorporate organic matter into soil\n- Implement split applications of nitrogen\n- Use controlled-release nitrogen sources\n- Consider foliar nitrogen application for quick response"
        },
        
        "Phosphorus Deficiency": {
            "name": "Phosphorus Deficiency",
            "symptoms": "- Dark green leaves with reddish-purple discoloration\n- Stunted root and shoot growth\n- Delayed maturity\n- Reduced tillering\n- Narrow, erect leaves\n- Poor grain development",
            "causes": "- Low soil phosphorus levels\n- Cold soil temperatures limiting uptake\n- Very high or low soil pH\n- Compacted soils\n- High levels of iron, aluminum, or calcium in soil",
            "treatment": "- Apply phosphate fertilizers (superphosphate, DAP)\n- Band application near seed at planting\n- Correct soil pH to optimum range (6.0-7.0)\n- Incorporate organic matter\n- Improve soil drainage and reduce compaction"
        },
        
        "Potassium Deficiency": {
            "name": "Potassium Deficiency",
            "symptoms": "- Yellowing and necrosis along leaf margins\n- Scorched appearance of leaf edges\n- Weakened stems and lodging\n- Increased susceptibility to drought and frost\n- Poor grain filling",
            "causes": "- Low soil potassium levels\n- Sandy soils with high leaching\n- Heavy clay soils that fix potassium\n- Imbalance with other cations (calcium, magnesium)\n- Excessive nitrogen application",
            "treatment": "- Apply potassium fertilizers (potassium chloride, potassium sulfate)\n- Balance nitrogen and potassium applications\n- Incorporate crop residues\n- Consider foliar application for immediate response\n- Improve soil organic matter content"
        },
        
        "Sulfur Deficiency": {
            "name": "Sulfur Deficiency",
            "symptoms": "- Uniform yellowing of young leaves\n- Reduced leaf size\n- Delayed maturity\n- Thin, spindly stems\n- Similar to nitrogen deficiency but affects new growth first",
            "causes": "- Low soil sulfur content\n- Reduced atmospheric sulfur deposition\n- High rainfall areas with leaching\n- Low organic matter\n- High-yielding crops depleting soil reserves",
            "treatment": "- Apply sulfur-containing fertilizers (ammonium sulfate, gypsum)\n- Incorporate organic matter\n- Use elemental sulfur in alkaline soils\n- Consider foliar application of sulfur solutions\n- Balance with nitrogen applications"
        },
        
        "Iron Deficiency": {
            "name": "Iron Deficiency",
            "symptoms": "- Interveinal chlorosis of young leaves\n- Distinct green veins with yellow tissue between\n- Entire leaf becomes pale yellow to white in severe cases\n- Reduced growth\n- Appears first on newer leaves",
            "causes": "- High soil pH (alkaline soils)\n- Calcareous soils with high calcium carbonate\n- Waterlogged conditions\n- Cool, wet weather\n- Excessive levels of manganese, zinc, or phosphorus",
            "treatment": "- Apply iron chelates (EDDHA, EDTA)\n- Foliar application of iron sulfate or chelates\n- Lower soil pH when possible\n- Improve soil drainage\n- Avoid excessive phosphorus application"
        },
        
        "Zinc Deficiency": {
            "name": "Zinc Deficiency",
            "symptoms": "- Chlorotic stripes on either side of the midrib\n- Stunted plants with shortened internodes\n- Reduced leaf size\n- 'Rosetting' of leaves in severe cases\n- Delayed maturity",
            "causes": "- Low soil zinc levels\n- High soil pH\n- High phosphorus levels\n- Cool, wet conditions\n- Sandy soils with low organic matter\n- Soils high in calcium carbonate",
            "treatment": "- Apply zinc sulfate or zinc chelates\n- Foliar application for quick response\n- Seed treatment with zinc\n- Maintain balanced phosphorus levels\n- Incorporate organic matter\n- Correct extremely high soil pH"
        },
        
        "Manganese Deficiency": {
            "name": "Manganese Deficiency",
            "symptoms": "- Interveinal chlorosis with a checkered pattern\n- Gray or tan necrotic lesions\n- 'Marsh spot' - brown spots in grain\n- Limp, drooping leaves\n- Primarily affects middle leaves",
            "causes": "- High soil pH (above 6.5)\n- Organic soils\n- Over-limed soils\n- Poor soil aeration\n- High iron levels\n- Dry soil conditions",
            "treatment": "- Apply manganese sulfate\n- Foliar application of manganese solutions\n- Lower soil pH when possible\n- Improve soil drainage\n- Apply in band rather than broadcast\n- Use acidifying nitrogen fertilizers"
        },
        
        "Boron Deficiency": {
            "name": "Boron Deficiency",
            "symptoms": "- Brittle, thickened leaves\n- Death of growing points\n- Stunted, malformed young leaves\n- Poor grain development\n- Short, thick stems\n- Reduced fertility",
            "causes": "- Low soil boron content\n- Drought conditions\n- Sandy, acidic soils with high leaching\n- High soil pH\n- Low organic matter\n- Excessive liming",
            "treatment": "- Apply boron fertilizers (borax, solubor)\n- Foliar application at low rates\n- Incorporate organic matter\n- Maintain proper soil moisture\n- CAUTION: Apply at low rates as toxicity range is narrow"
        },
        
        "Copper Deficiency": {
            "name": "Copper Deficiency",
            "symptoms": "- Yellowing or chlorosis of leaf tips\n- Twisted leaves and stems\n- 'Pig-tailing' or spiraling of leaf tips\n- Impaired reproductive development\n- Empty grain heads\n- Delayed heading",
            "causes": "- Organic soils and peats\n- Sandy soils\n- High soil pH\n- High levels of nitrogen and phosphorus\n- Excessive zinc or iron",
            "treatment": "- Apply copper sulfate or copper chelates\n- Foliar application of copper solutions\n- Soil application before planting\n- Balance other micronutrients\n- Add to NPK fertilizers at sowing\n- Maintain balanced soil pH"
        }
    }
    
    # Return information for the requested deficiency
    if deficiency_name in deficiency_database:
        return deficiency_database[deficiency_name]
    else:
        # Return a generic response for unknown deficiencies
        return {
            "name": "Unknown Condition",
            "symptoms": "The specific condition could not be identified with confidence.",
            "causes": "Multiple factors could contribute to the observed symptoms.",
            "treatment": "Consult with an agricultural extension specialist for in-person diagnosis."
        }
