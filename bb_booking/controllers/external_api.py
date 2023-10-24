from odoo import http
from odoo.http import request, Response
from odoo.tools.safe_eval import json
#*****************************************prova*****************






#https://odoo16-prenotazione-bb.unitivastaging.it/api/test


#*********************route****************************
class RoomBookingController(http.Controller):

    @http.route('/api/test', cors='*', auth='public', methods=['GET', 'POST'], csrf=False, website=False, type='json')
    def handle_custom_endpoint(self, **kw):
        json_data = request.httprequest.data
        try:
            data_dict = json.loads(json_data)
            content = json.loads(data_dict.get("content"))

        except ValueError:
            return "Errore nella formattazione dei dati JSON"

            # Estrai il valore del campo 'checkin' dal dizionario dei dati
        refer = content.get("refer")
        guestsList = content.get("guestsList")
        roomGross = content.get("roomGross")
        totalGuest = content.get("totalGuest")
        guests = content.get("guests")
        checkin = guests[0].get("checkin")
        checkout = guests[0].get("checkout")


        response_data = {
            "refer": refer,
            "guestsList": guestsList,
            "prezzo": roomGross,
            "ospiti" : totalGuest,
            "checkin" : checkin,
            "checkout": checkout

        }

        # room_booking_obj = request.env['account.move']
        # new_invoice = room_booking_obj.sudo().create({
        #     'refer': refer,
        #     'checkin': checkin,
        #     'checkout': checkout,
        #     'totalGuest': totalGuest,
        #     'roomGross': roomGross,
        #     'partner_id': 36
        #     # Altri campi del tuo modello che devono essere impostati
        # })


        return "Fattura creata con successo"



        return Response(json.dumps(response_data), content_type='application/json')
#********************************************************************************************************
# else:
#     print("fallito")
# from odoo import http
# from odoo.http import request
# import json
#
# class ThirdPartyConnector(http.Controller):
#     @http.route('/third_party_connector/receive_data', type='json', auth='user', methods=['POST'], csrf=False)
#     def receive_data(self, **kwargs):
#         data = request.jsonrequest
#
#         if data:
#             try:
#                 model = "account.move"
#                 type = data.get('type')
#
#                 # Estrazione dati dal JSON
#                 content_data = json.loads(data.get('content')) if data.get('content') else {}
#
#                 # Fiedls di interesse
#                 fields = {
#                     'refer': content_data.get('refer'),
#                     'checkin': content_data.get('checkin').split('T')[0] if content_data.get('checkin') else False,
#                     'checkout': content_data.get('checkout').split('T')[0] if content_data.get('checkout') else False,
#                     'totalGuest': content_data.get('totalGuest'),
#                     'totalChildren': content_data.get('children'),
#                     'totalInfants': content_data.get('infants'),
#                     'rooms': content_data.get('rooms'),
#                     'roomGross': content_data.get('roomGross'),
#                     # altri fields possono essere aggiunti qui in base alle necessità
#                 }
#
#                 if type == 'RESERVATION_CREATED':
#
#                     fields['state'] = 'draft'
#                     record = request.env[model].create(fields)
#                     return {'success': True, 'record_id': record.id}
#
#                 elif type in ['RESERVATION_CANCELLED', 'RESERVATION_CONFIRMED']:
#                     # cerca il record esistente tramite ID di riferimento, aggiorna lo stato e lascia invariati gli altri campi
#                     refer_id = fields.get('refer')
#                     record = request.env[model].search([('refer', '=', refer_id)])
#
#
#
#                 else:
#                     return {'error': 'Invalid type'}
#
#             except Exception as e:
#                 return {'error': str(e)}
#
#         return {'error': 'Invalid data'}