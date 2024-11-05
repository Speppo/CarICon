import pandas as pd

# Carica il dataset
dataset = pd.read_csv('C:/Users/Speppo/PycharmProjects/CarICon/datasets/Car_Dataset_1945-2020.csv', dtype=str)
dataset = dataset.rename(columns={'Modle': 'Model'})

# Elimino caratteristiche che non servono ai fini dell'interrogazione
caratteristiche_da_eliminare = ['id_trim', 'Trim', 'Body_type', 'load_height_mm', 'number_of_seats', 
                               'wheel_size_r14', 'ground_clearance_mm', 'trailer_load_with_brakes_kg',
                               'payload_kg', 'back_track_width_mm', 'front_track_width_mm', 'clearance_mm',
                               'full_weight_kg', 'front_rear_axle_load_kg', 'cargo_compartment_length_width_height_mm',
                               'cargo_volume_m3', 'overhead_camshaft', 'compression_ratio', 'engine_placement',
                               'cylinder_bore_and_stroke_cycle_mm', 'max_power_kw', 'presence_of_intercooler',
                               'bore_stroke_ratio', 'turning_circle_m', 'mixed_fuel_consumption_per_100_km_l',
                               'range_km', 'emission_standards', 'CO2_emissions_g/km', 'rear_brakes', 'front_brakes',
                               'steering_type', 'car_class', 'country_of_origin', 'number_of_doors', 'safety_assessment',
                               'rating_name', 'battery_capacity_KW_per_h', 'electric_range_km', 'charging_time_h']
dataset = dataset.drop(caratteristiche_da_eliminare, axis=1)

# In boost_type, inserisco none dove non ci sono valori
dataset['boost_type'] = dataset['boost_type'].fillna('none')

# Rinomino valori 'petrol' e 'Gas (Gasoline)' in 'Fuel' nella colonna 'engine_type'
dataset['engine_type'] = dataset['engine_type'].replace({'petrol': 'Fuel', 'Gas (Gasoline)' : 'Fuel'})

# Converto valori tipo 0,0 in 0.0 (cambio virgola con punto)
dataset['fuel_tank_capacity_l'] = dataset['fuel_tank_capacity_l'].str.replace(',', '.')
dataset['rear_track_mm'] = dataset['rear_track_mm'].str.replace(',', '.')
dataset['curb_weight_kg'] = dataset['curb_weight_kg'].str.replace(',', '.')
dataset['max_speed_km_per_h'] = dataset['max_speed_km_per_h'].str.replace(',', '.')
dataset['maximum_torque_n_m'] = dataset['maximum_torque_n_m'].str.replace(',', '.')
dataset['front_track_mm'] = dataset['front_track_mm'].str.replace(',', '.')
dataset['max_trunk_capacity_l'] = dataset['max_trunk_capacity_l'].str.replace(',', '.')

# Elimino le righe con almeno un campo vuoto e le righe doppie
dataset = dataset.dropna()
dataset = dataset.drop_duplicates()

# Sostituisco gli spazi con i trattini bassi in tutti i nomi di colonna e converte tutto in minuscolo
dataset.columns = dataset.columns.str.replace(' ', '_').str.lower()
dataset = dataset.apply(lambda x: x.str.replace(' ', '_').str.lower())

dataset['generation'] = dataset['generation'].apply(lambda x: 'h_' + x)

dataset['model'] = dataset['model'].apply(lambda x: 'h_' + x)

dataset['fuel_grade'] = dataset['fuel_grade'].apply(lambda x: 'h_' + x)

dataset['series'] = dataset['series'].apply(lambda x: 'h_' + x)

# Rimuovo parentesi quadre dalla colonna
dataset['generation'] = dataset['generation'].str.replace(r'\[|\]', '', regex=True)

dataset['generation'] = dataset['generation'].str.replace('.', '_')

dataset['model'] = dataset['model'].str.replace('.', '')

dataset['series'] = dataset['series'].str.replace('.', '_')

# Adattamento del dataset: replaces
dataset = dataset.apply(lambda x: x.str.replace(r'\(|\)', '', regex=True))

dataset = dataset.apply(lambda x: x.str.replace('-', '_'))

dataset = dataset.apply(lambda x: x.str.replace(',', '_and'))

dataset = dataset.apply(lambda x: x.str.replace('+', '_and'))

dataset = dataset.apply(lambda x: x.str.replace('/', '_'))

dataset = dataset.apply(lambda x: x.str.replace("'", ''))

dataset = dataset.apply(lambda x: x.str.replace('"', ''))

# Aggiungo una colonna con indice autoincrementale
dataset.insert(0, 'ID', range(1, 1 + len(dataset)))

# Salvo dataset aggiornato
dataset.to_csv('datasets/preprocessed.csv', index=False)