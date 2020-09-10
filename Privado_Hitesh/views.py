from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .mongo_connector import MongoConnector


@csrf_exempt
def template_endpoint(request, customer_id):
    # ------Check for a valid customer_id----------#
    try:
        int(customer_id)
    except ValueError:
        return render(request, 'invalid_id.html', {'id': customer_id})

    # ------Connecting to the database-------------#
    mongo = MongoConnector()

    if request.method == 'POST':
        template_union = mongo.templates.find({'type': 'system'})
        field_list = []
        for i, t in enumerate(template_union):
            field_list += t['fields']  # Appending feilds
            if i == 0:
                template_copy = t

        # ------------Updating urls with correct customer_id-------------#
        field_list[5]['options_url']['url'] = field_list[5]['options_url']['url'].replace('<customer_id>',
                                                                                          str(customer_id))
        field_list[7]['options_url']['url'] = field_list[7]['options_url']['url'].replace('<customer_id>',
                                                                                          str(customer_id))

        template_copy['customerId'] = customer_id
        template_copy['fields'] = field_list
        template_copy['type'] = 'customer'
        del template_copy['_id']

        # ---------inserting data for a new customer_id in database------------#
        mongo.templates.replace_one(template_copy, template_copy, upsert=True)

        params = {'customer_id': customer_id, 'template': template_copy}
        return render(request, 'post_request.html', params)

    elif request.method == 'GET':
        template = mongo.templates.find_one({'customerId': customer_id})
        if template:
            return HttpResponse(f'<h1>Received GET request for customer: {customer_id}</h1><br><p>{template}</p>')
        else:
            return render(request, '404_not_found.html', {'id': customer_id})

    else:
        return render(request, '400_bad_request.html')


def home(request):
    #--------inserting Templates---------#
    mongo = MongoConnector()
    return HttpResponse('<h1>Templates added to the Database: "te", in Collection:"templates"</h1>')
