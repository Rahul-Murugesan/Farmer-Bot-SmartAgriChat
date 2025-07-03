few_shots = [
    {
        'Question': "What is the current temperature in field A101?",
        'SQLQuery': "SELECT temperature FROM field_data WHERE field_id = 'A101'",
        'SQLResult': "Result of the SQL query",
        'Answer': "32°C"
    },
    {
        'Question': "Can you tell me the humidity level in field B205?",
        'SQLQuery': "SELECT humidity FROM field_data WHERE field_id = 'B205'",
        'SQLResult': "Result of the SQL query",
        'Answer': "68%"
    },
    {
        'Question': "What is the soil moisture status for my field C309?",
        'SQLQuery': "SELECT soil_moisture FROM field_data WHERE field_id = 'C309'",
        'SQLResult': "Result of the SQL query",
        'Answer': "Moderate"
    },
    {
        'Question': "Will it rain today in field D110?",
        'SQLQuery': "SELECT weather_prediction FROM field_data WHERE field_id = 'D110'",
        'SQLResult': "Result of the SQL query",
        'Answer': "Yes, light rain expected"
    },
    {
        'Question': "Is the crop health prediction good for my field A101?",
        'SQLQuery': "SELECT health_prediction FROM field_data WHERE field_id = 'A101'",
        'SQLResult': "Result of the SQL query",
        'Answer': "Healthy"
    },
    {
        'Question': "Is the irrigation system turned on in field B205?",
        'SQLQuery': "SELECT water_irrigation_status FROM field_data WHERE field_id = 'B205'",
        'SQLResult': "Result of the SQL query",
        'Answer': "Yes"
    },
    {
        'Question': "Give me a summary of all data for field C309",
        'SQLQuery': "SELECT temperature, humidity, soil_moisture, weather_prediction, health_prediction, water_irrigation_status FROM field_data WHERE field_id = 'C309'",
        'SQLResult': "Result of the SQL query",
        'Answer': "Temperature: 30°C, Humidity: 60%, Soil Moisture: Moderate, Weather: Sunny, Health: Good, Irrigation: Off"
    }
]
