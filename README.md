The given data *'coupons_ner.csv'* contains OfferDetails(text) for various coupons.
The task is to extarct FaceValue of the coupon i.e. the value of total money saved by coupon.

The code in ***face_val.py*** reads the OfferDetails from *coupons_ner.csv* into a pandas dataframe, extracts FaceValue from it(if available) and stores in a new column named *'faceValue'*. Finally it saves the result into a new CSV file *facevalue.csv*.
