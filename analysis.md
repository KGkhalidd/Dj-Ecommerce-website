   
products app ->    
                Products :
                    - name
                    - flag [new - sale - feature]
                    - image , images
                    - price
                    - reviews
                    - subtitle
                    - tags
                    - brand
                    - sku
                    - category

                Category :
                    - name
                    - image


                brand :
                    - name
                    - image


orders app ->

                orders :
                    
                    - code
                    - user
                    - order_time
                    - delivery_time
                    - status [received - processed - shipped - delivered ]

                order detail : 
                    - order
                    - product
                    - quantity
                    - price 
                    - total

settings app -> 

                manage details of the website like
                logo - phone numbers - copyrights ets


accounts app -> 

                manage user and his details 


                User :
                    - username 
                    - email 
                    - address
                    - image 
                    - contact number 
                    - favorites

                    django user have :
                                    - user name 
                                    - first and last name
                                    - password 
                                    - email 

                we have 3 types of users :
                1- Base user 
                2- abstract user 
                3- one to one model -> we will use this 


                we will split phone number in class cause it is multiple
                
------------------------------------------------------
signals in django -> once user make sign up the profile will created
types of signals :
                pre -> before  delete init save
                post -> after  delete init save
                many2many



