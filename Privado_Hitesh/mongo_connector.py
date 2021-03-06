
from pymongo import MongoClient
import json

Template1 = json.loads(r'''{
	"type": "system",
	"entity": "entity",
	"customerId": "system",
	"law" : "base",
	"fields" : [
		{ "field" : "name", "label" : "Name", "data_type" :"short-text", "default" : "Type name here..", "field_type":	"basic_details", "field_type_label":	"Basic Details", "is_removable" : false, "mandatory": true},
		{ "field" : "description", "label" : "Description", "data_type" :"long-text", "default" : "Type description here..", "field_type":	"basic_details", "field_type_label":	"Basic Details", "is_removable" : false, "mandatory": false},
		{ "field" : "entity_type", "label" : "Entity Type", "data_type" :"options", "default" : "", "field_type":	"basic_details", "field_type_label":	"Basic Details", "is_removable" : false, "mandatory": false,
			"options_list":[
				"Affiliate", "Client", "Holding Company", "Regulatory Body", "Subsidiary"
			    ]
		},
		{ "field" : "location", "label" : "Location", "data_type" :"options", "default" : "", "field_type":	"basic_details", "field_type_label":	"Basic Details", "is_removable" : false, "mandatory": false,
			"options_url": {
				"url" : "dm/geos",
				"request_type" : "GET"
			    }
		}
    ]
    }''')

Template2 = json.loads(r'''{
	"type": "system",
	"entity": "entity",
	"customerId": "system",
	"law" : "GDPR",
	"fields" : [
		{ "field" : "address", "label" : "Address", "data_type" :"long-text", "default" : "Type address here..", "field_type":	"contact_details", "field_type_label":	"Contact Details", "is_removable" : false, "mandatory": false},
		{ "field" : "representative", "label" : "Representative", "data_type" :"options", "default" : "Type the representative name here..", "field_type":	"contact_details", "field_type_label":	"Contact Details", "is_removable" : false, "mandatory": false,
			"options_url": {
				"url" : "dm/customer/<customer_id>/users",
				"request_type" : "GET"
			}
		}
	]
}''')

Template3 = json.loads(r'''{
	"type": "system",
	"entity": "entity",
	"customerId": "system",
	"law" : "CCPA",
	"fields" : [
		{ "field" : "representative_contact_details", "label" : "Representative Contact Details", "data_type" :"long-text", "default" : "Type contact details here..", "field_type":	"contact_details", "field_type_label":	"Contact Details", "is_removable" : false, "mandatory": false},
		{ "field" : "data_protection_officer", "label" : "Data Protection Officer", "data_type" :"options", "default" : "Type the data protection officer name here..", "field_type":	"contact_details", "field_type_label":	"Contact Details", "is_removable" : false, "mandatory": false,
			"options_url": {
				"url" : "dm/customer/<customer_id>/users",
				"request_type" : "GET"
			}
		},
		{ "field" : "dpo_contact_details", "label" : "Data Protection Officer Contact Details", "data_type" :"long-text", "default" : "Type contact details here..", "field_type":	"contact_details", "field_type_label":	"Contact Details", "is_removable" : false, "mandatory": false}
	]
}''')


class MongoConnector:

    def __init__(self):
        self.client = MongoClient()
        self.te = self.client['te']
        self.templates = self.te['templates']
        self.templates.replace_one(Template1, Template1, upsert=True)
        self.templates.replace_one(Template2, Template2, upsert=True)
        self.templates.replace_one(Template3, Template3, upsert=True)

'''
    def find(self,db, collection, name):
        db = client[db]
        collection = db[collection]
        response = collection.find_one({"name":str(name)})
        return dumps(response)
'''