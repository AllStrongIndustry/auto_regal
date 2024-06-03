import pandas as pd 

# Get the file path
src_file_path = input('Enter the file path: ')

# Get the folder path from the file path
folder_path_list = src_file_path.split("\\")[:-1]
folder_path = '\\'.join(folder_path_list)

# Extract the file name from the file path
file_name = src_file_path.split('\\')[-1]
file_name_without_extension = file_name.split('.')[0]
purchase_order_file_name = file_name_without_extension +'_output.xlsx'

as_regal_file = r"as_regal_price.csv"
# read the file with csv
original_df = pd.read_csv(src_file_path, sep='\t')
# read the file with csv
as_regal_df = pd.read_csv(as_regal_file)
# joing two dataframes left on the sku right on the regal_sku
merge_df = pd.merge(original_df, as_regal_df, left_on='sku', right_on='regal_sku', how='left')

merge_df = merge_df[['order-id', 'buyer-email','buyer-name','buyer-phone-number','ship-address-1','ship-address-2','ship-city','ship-state','ship-postal-code','ship-country','origin_sku','quantity-purchased','sale_Price']]
# rename the header of the columns
merge_df["Customer No."] = "REGAL"
merge_df["Ship Method"] = "FEDX"
new_head_mapping = {
    'order-id':'Purchase Order',
    'buyer-email':'Email',
    'buyer-name':'Ship To Name',
    'buyer-phone-number':'Phone Number',
    'ship-address-1':'Ship To Address 1',
    'ship-address-2':'Ship To Address 2',
    'ship-city':'Ship to City',
    'ship-state':'Ship to State',
    'ship-postal-code':'Ship to ZipCode',
    'ship-country':'Ship to Country',
    'origin_sku':'Item Code',
    'quantity-purchased':'Item Qty',
    'sale_Price':'Item Price'
}
merge_df = merge_df.rename(columns=new_head_mapping)
# change order for the cloumn
new_order = ['Customer No.', 'Purchase Order',  'Ship Method', 'Ship To Name', 'Ship To Address 1', 'Ship To Address 2','Ship to ZipCode', 'Ship to City', 'Ship to State', 'Ship to Country',  'Phone Number', 'Email', 'Item Code', 'Item Qty', 'Item Price']
merge_df = merge_df[new_order]
merge_df['order-id'] = ''
merge_df.to_excel(purchase_order_file_name, index=False)