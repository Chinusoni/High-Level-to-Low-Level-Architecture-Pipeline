from django.shortcuts import render
from .models import Blueprint
from .utils import generate_tech_specs

def index(request):
    spec = None
    if request.method == "POST":
        user_input = request.POST.get("requirement")
        
        # Trigger Gemini 3.1 Flash Lite
        data = generate_tech_specs(user_input)
        
        if data:
            # Save the structured response to our database
            spec = Blueprint.objects.create(
                requirement=user_input,
                modules=data.get('modules', []),
                schema_sql=data.get('database_tables', ''),
                pseudocode=data.get('logic_pseudocode', '')
            )
            
    return render(request, 'index.html', {'spec': spec})