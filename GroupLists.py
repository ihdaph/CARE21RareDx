#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 22:00:46 2021

@author: kianaamaral
"""
AsianGroups = ['Asia', 'Asian', 'Mongolia', 'Chinese', 'Japan', 'Filipino', 
               'Pacific', 'China', 'Korea', 'Vietnam', 'Philippines', 'Taiwan', 
               'Borneo', 'Brunei', 'Cambodia', 'Indochina', 'Indonesia', 'Laos', 
               'Malaysia', 'Singapore', 'Thailand', 'Timor-Leste', 'Indian', 'India', 
               'Bangladesh', 'Bhutan', 'Middle East', 'West Bank', 'Gaza', 'Palestine', 
               'Afghanistan', 'Bahrain', 'Iran', 'Iraq', 'Israel', 'Nepal', 'Pakistan', 
               'Sri Lanka', 'Jordan', 'Kuwait', 'Leban', 'Qatar', 'Saudi Arabia', 
               'Syria', 'Turkey', 'United Arab Emirates', 'Abu Dhabi', 'Yemen']           

for i in range(len(AsianGroups)):
    lower = AsianGroups[i].lower() 
    AsianGroups.append(lower)
    


HispanicGroups = ['Hispanic', '“Caribbean Region”', 'Latin', 
                  'South America', 'Central America', 'Latin America', 'South America', 
                  'Hispanic', 'Spanish American', 'Latino', 'Cuba', 'Cuba', 'Latina', 'Puerto Rican',
                  '“Puerto Rico”', 'Mexico', 'Mexican', 'Caribbean', 'Belize', 'Costa', 'Salvador', 
                  'Guatemala', 'Honduras', 'Nicaragua', 'Panama', 'Argentins', 'Bolivia', 'Brazil', 
                  'Chile', 'Chilean', 'Columbia', 'Ecuador', 'Guiana', 'Guyana', 'Peru', 
                  'Paraguay', 'Suriname', 'Uruguay', 'Venezuela']

for i in range(len(HispanicGroups)):
    lower = HispanicGroups[i].lower() 
    HispanicGroups.append(lower)
    
    

IndigenousGroups = ['Indigenous', 'Native', 'Indian', 'Inuit', 
                    'Aboriginal', 'Kalaallit', 'Inupiat', 
                    'Aleut', 'Eskimo', 'Tribe', 'Reservation',
                    'Amerinds', 'Metis']

for i in range(len(IndigenousGroups)):
    lower = IndigenousGroups[i].lower() 
    IndigenousGroups.append(lower)
    
    

AfricanGroups = ['African', 'Black', 'Blacks', 'Afro', 'Africa', 'Africa', 'Sudan', 
                 'Sahara', 'Algeria', 'Egypt', 'Libya', 'Morocco', 'Tunisia', 'Cairo', 'Rabat', 
                 'Casablanca', 'Tripoli', 'Algiers', 'Fes', 'Marrakesh', 'Tunis', 'Carthage', 
                 'Tangier', 'Kairouan', 'Essaouira', 'Luxor', 'Bizerte', 'El Aaiun', 'Sousse', 
                 'Oran', 'Annaba', 'Constantine', 'Biskra', 'Chefchaoouen', 'Skikda', 'Sheikh', 
                 'Volubilis', 'Oued', 'Meknes', 'Hippo Regius', 'Djemila', 'Sfax', 'Tataouine', 
                  'Benhaddou', 'Benghazi', 'Juba', 'Tamanrasette', 'Merzouga', 
                 'Djem', 'Oujda', 'Matmata', 'Ghat', 'Tabessa', 'Giza', 'Marj', 'Ifrane', 'Agadir', 
                 'Tetouan', 'Kheima', 'Tobruk', 'Khartoum', 'Nyala', 'Kassala', 'Ubayyid', 
                 'Kosti', 'Madani', 'Qadarif', 'Al-Fashir', 'Daein', 'Damazin', 'Geneina', 'Merowe', 
                 'Burundi', 'Comoros', 'Djibouti', 'Eritrea', 'Ethiopia', 'Kenya', 'Madagascar', 
                 'Malawi', 'Mauritius', 'Mayotte', 'Mozambique', 'Rwanda', 'Seychelles', 
                 'Somalia', 'Sudan', 'Tanzania', 'Uganda', 'Zambia', ' Zimbabwe', 'Crozet Islands', 
                 'Iles Crozet', 'Eparses', 'Addis Ababa', 'Asmara', 'Anananarivo', 
                 'Arusha', 'Axum', 'Bahir Dar', 'Berbera', 'Bulawayo', 'Dese', 'Eldoret', 'Garissa', 
                 'Geita', 'Gondar', 'Hargeisa', 'Hargeysa', 'Hola', 'Jinja', 
                 'Iringa', 'Kigoma', 'Jimma', 'Korogwe', 'Nairobi', 'Salaam', 'Mombasa', 'Mogadishu', 
                 'Dodomoa', 'Bujumbura', 'Mbeya', 'Lusaka', 'Harare ', ' Kakamega', 'Kampala', 'Kigali', 
                 'Kire Dawa', 'Kikuyu', 'Kisumu', 'Kitale', 'Kitui', 'Lilongwe', 'Victoria', 
                 'Lake Tanganyika', 'Lamu', 'Lodwar', 'Lokichogio', 'Malindi', 'Machakos', 
                 'Marka', 'Machakos', 'Maputo', 'Maralal', 'Mekele', 'Meru', 'Musoma', 'Mtwara', 
                 'Mumias', 'Moshi', 'Moroni', 'Morogoro', 'Mwanza', 'Naivasha', 'Nanyuki', 'Nakuru ', 
                 'Namanga', 'Nyeri', 'Port Louis', 'Puntland', 'Nyahururu', 'Kismayo', ' Ruiru', 
                 'Rwenzori Mountains', 'Sinyanga', 'Songea', 'Tanga', 'Tabora', 'Voi', 'Webuye', 
                 'Zanzibar', 'Adiharush', 'Ali-Addeh', 'Alinjugur', 'Buramino', ' Dadaab', 'Dagahaley', 
                 'Dollo Ado', 'Fugnido', 'Hagadera', 'Hilaweyn', 'Ifo', 'Kakuma', 'Kambioos', 'Kayaka Ii', 
                 'Kobe', 'Kyangwali Nakivale', 'Nyarugusu', ' Wad Sherife', 'Bokolmanyo', 'Melkadida', 
                 'Rwamanja ', 'Benin', 'Burkina', 'Cape Verd', 'Cabo Verd', 'Ivory Coast', 'Cote Divoire', 
                 'Gambia', 'Ghana', 'Guinea', 'Bissau', 'Liberia Map', 'Malian', 'Mauritania', 
                 'Nigeria', 'Senegal', 'Sierra Leon', 'Togo', 'Lagos', 'Accra', 'Abidjan', 'Dakar', 
                 'Abobo', 'Abuja', 'Freetown', 'Ouagadougou', 'Conakry', 'Lome', 'Bamako', 'Cotonou', 
                 'Kumasi', 'Monrovia', 'Ibadan', 'Kano', 'Port Harcourt', 'Benin City', 'Porto Novo', 
                 'Niamey', 'Yamoussoukro', 'Banjul', 'Timbuktu', 'Djenne', 'Abomeyu', 'Zaria', 'Tamale', 
                 'Jos', 'Cape Coast', 'Maidugul', 'Aba', 'Gao', 'Calabar', 'Warri', 'Maiduguri', 
                 'Bobo Dioulasso', 'Parakou', 'Djougou', 'Bohicon', 'Sekondi Takoradi', 'Sunyani', 
                 'Obuasi', 'Teshie', 'Tema', 'Sikasso', 'Kalabankoro', 'Nouakchott', 
                 'Dakhlet Nouadhibou', 'Benin', 'Port Harcourt', 'Ilorin', 'Kaduna', 
                 'Enugu', 'Ikorodu', 'Onitsha', 'Bauchi', 'Akure', 'Abeokuta', 'Sokoto', 'Bouake', 
                 'Makeni', 'Kaduan', 'Sosgbo', 'Osogbo', 'Gombe', 'Ilesa', 'Badagry', 'Makurdi', 'Sagamu', 
                 'Iseyin', 'Obbomosho', 'Awka', 'Ado Ekiti', 'Nsukka', 'Ikeja', 'Katsina', 'Okene', 'Lafia', 
                 'Minna', 'Ondo City', 'Umuahia', 'Calabar', 'Yola', 'Pikine', 'Touba', 'Thies', 
                 'Saint Louis', 'Kolak', 'Ziguinch', 'San Pedro', 'Bandama', 'Daloa', 'Owerri', 'Kandi',
                 'Ifi', 'Dakar', 'Ogbomosho', 'Divo', 'Korhogo', 'Angola', 'Cameroon', 'Chad', 'Tchad', 'Congo', 
                 'Drc', 'Equatorial Guinea', 'Gabon', 'Sao Tome', 'Principe', 'Luanda', 'Lobito', 'Kuito', 
                 'Huambo', 'Malanje', 'Douala', 'Yaounde', 'Bamenda', 'Garoua Of Bafoussam', 'Nganoundere', 
                 'Maroua', 'Kouosseri', 'Buena', 'Kumba', 'N Djamena', 'Moundou', 'Bangui', 'Bimbo', 'Brazzaville', 
                 'Point Noire', 'Kinshasa', 'Lubumbashi', 'Leopoldville', 'Elizabethville', 'Mbuji Mayi', 'Bakwanga', 
                 'Bukavu', 'Costermansville', 'Kananga', 'Luluabourg', 'Kisangani', 'Stanleyville', 
                 'Tshikapa', 'Koalwezi', 'Likasi', 'Jadotville', 'Goma', 'Kikwit', 'Uvira', 'Bunia', 
                 'Mbandaka', 'Coquilhatville', 'Matadi', 'Butembo', 'Kabinda', 'Mwene Ditu', 'Isiro', 
                 'Paulis', 'Boma', 'Kindu', 'Bata', 'Malabo', 'Libreville', ' Botswana', 'Lesotho',
                 'Malawi', 'Mozambiq', 'Namibia', 'Swaziland', 'Zambia', 'Zimbabwe', 'Zulu', 'Tsonga',
                 'Xhosa', 'Swazi', 'Ndebele', 'Tswana', 'Sotho', 'Shona People', 'Balunda', 'Mbundu', 'Ovimbundu', 
                 'Chaga', 'Sukuma', 'Pretoria', 'Cape Town', 'Johannesburg', 'Durban', 'Port Elizabeth', 'Bloemfontein',
                 'Windhoek', 'Maseru', 'Pietermaritz', 'Kimberley', 'Nespruit', 'Soweto', 'Polokwane', 'Limpopo', 
                 'Rustenburg', 'Mahikeng', 'Oudtshroom', 'Stellenbosch', 'Paarl', 'Gaborone', 'Luanda', 'Cabinda', 'Huambo', 
                 'Lubango', 'Kuit', 'Malanje', 'Lobito', 'Lilongwe', 'Blantyre', 'Mzuzu', 'Maputo', 'Matola', 'Beira', 
                 'Nampula', 'Chimoio', 'Nacala', 'Quelimane', 'Lusaka', 'Kitwe', 'Ndola', 'Kabwe', 'Copperbelt Harare', 
                 'Bulawayo', 'Chitungwiza', 'Mutare', 'Masvingo', 'Monashonaland', 'Manicaland']

for i in range(len(AfricanGroups)):
    lower = AfricanGroups[i].lower() 
    AfricanGroups.append(lower)