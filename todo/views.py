from django.shortcuts import HttpResponse

def task_create(request):
    html_response = """
    <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yangi Vazifa Yaratish</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 50px;
            background-color: #f9f9f9;
        }

        form {
            width: 50%; /* Formani chap tomonda o'rnatamiz */
            margin: 0; /* Formani markazlashtirmaslik uchun marginni nol qilamiz */
            background: #ffffff;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .form-group {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }

        .form-group label {
            width: 30%;
            font-size: 16px;
            font-weight: bold;
            text-align: right;
            margin-right: 10px;
        }

        .form-group input,
        .form-group textarea,
        .form-group select {
            width: 70%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        textarea {
            min-height: 80px;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 10px;
        }

        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Yangi Vazifa Yaratish</h1>
    <form action="/submit" method="POST">
        <div class="form-group">
            <label for="vazifa_nomi">Vazifa nomi:</label>
            <input type="text" id="vazifa_nomi" name="vazifa_nomi" required>
        </div>

        <div class="form-group">
            <label for="tavsif">Tavsif:</label>
            <textarea id="tavsif" name="tavsif" required></textarea>
        </div>

        <div class="form-group">
            <label for="muddat">Muddati:</label>
            <input type="date" id="muddat" name="muddat" required>
        </div>

        <div class="form-group">
            <label for="muhimlik_darajasi">Muhimlik darajasi:</label>
            <select id="muhimlik_darajasi" name="muhimlik_darajasi" required>
                <option value="past">Past</option>
                <option value="orta">O'rta</option>
                <option value="yuqori">Yuqori</option>
            </select>
        </div>

        <button type="submit">Vazifani saqlash</button>
    </form>
</body>
</html>

    """
    return HttpResponse(html_response)

