from Tkinter import *
import sqlite3
from tkMessageBox import *
import random
import splash


splash.splashscreen()
admin=Tk()
a=PhotoImage(file='tar.gif')
Label(admin,image=a).grid(row=1,column=3)
admin.configure(bg='White')


Label(admin,text='Administrator Login Panel',font='times 20 bold italic',bd=7,relief=SUNKEN).grid(row=0,column=2,columnspan=5)
Label(admin,text='USERNAME',font='times 10 bold italic',bd=3).grid(row=2,column=2,sticky='W')
a1=Entry(admin,bd=5,bg='Steel Blue')
a1.grid(row=2,column=4)

Label(admin,text="PASSWORD",font='times 10 bold italic',bd=3).grid(row=4,column=2,sticky='W')
a2=Entry(admin,show='*',bd=5,bg='Steel Blue')
a2.grid(row=4,column=4)
def login():
    if((a1.get())=="161B258" and (a2.get())=='python'):
        showinfo('Welcome',"Your Entry is Successful")
        admin.destroy()

        root=Tk()
        root.configure(bg='Blanched Almond')
        root.geometry("1600x800+0+0")
        root.title('GANPATI HYUNDAI')

        Tops = Frame(root,width=1600,bg='Blanched Almond',relief=SUNKEN)
        Tops.pack(side=TOP)

        fm1=Frame(root,width=300,height=700,bd=5,bg='Light Steel Blue',relief=SUNKEN)
        fm1.pack()

        Label(Tops,font=('arial',30,'bold'),text='GANPATI HYUNDAI',fg='Royal Blue',relief=SUNKEN,bd=20,anchor='w').grid(row=0,column=0)

        Label(Tops,font=('arial',13,),text="AIRPORT ROAD--VARANASI (221005)\n Contact-+91-9874563210,+91-9634521870    Email:- connecthyundai@hotmail.com\n#ROAD CHASERS",fg='Dark Slate Gray',relief='ridge',anchor='w').grid(row=1,column=0)

        Label(Tops,font=('arial',15,'bold'),text='nEW THINKING. \n nEW POSSIBILITES.',fg='Indian Red',anchor='w',relief='solid').grid(row=2,column=0)

        def suv():
            
            rootsuv=Toplevel()
           
            rootsuv.configure(bg='Thistle')
            rootsuv.geometry("1600x800+0+0")
            rootsuv.title('SUV')

            fsuv1=Frame(rootsuv,bd=5,bg='Light Steel Blue',relief=SUNKEN)
            fsuv1.pack(side=LEFT)

            vrsuv=IntVar()

            Label(fsuv1,text="RULE THE ROAD'S WITH \nALL NEW POWERFUL SUV'S",font='arial 25',fg='Indian Red',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
 
            Radiobutton(fsuv1,text='Hyundai TUCSON 4wd \n Designed To RULE',variable=vrsuv,value=1,font='times 20 bold').grid(row=3,column=3,padx=5,pady=5)
            Radiobutton(fsuv1,text='Hyundai CREATA \n The Perfect SUV',variable=vrsuv,value=2,font='times 20 bold').grid(row=6,column=3,padx=5,pady=5)
            Radiobutton(fsuv1,text='Hyundai SantaFE \n The Dynamic POWERDRIFT',variable=vrsuv,value=3,font='times 20 bold').grid(row=9,column=3,padx=5,pady=5)


            def viewsuv():
                
                
                if vrsuv.get()==1:
                    fsuv2=Frame(rootsuv,bd=5,bg='Light Steel Blue',height=6,relief=SUNKEN)
                    fsuv2.grid(row=1,column=2,padx=750)

                    Label(fsuv2,text="2WD MT Petrol",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=1,column=0,padx=30)
                    Label(fsuv2,text="2WD AT GL Petrol",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=2,column=0,padx=30)
                    Label(fsuv2,text="2WD MT Diesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=3,column=0,padx=30)
                    Label(fsuv2,text="2WD AT GL Diesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=4,column=0,padx=30)

                    Label(fsuv2,text="Rs:- 18.08 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=1,column=2,padx=30)
                    Label(fsuv2,text="Rs:- 20.99 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=2,column=2,padx=30)
                    Label(fsuv2,text="Rs:- 21.26 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=3,column=2,padx=30)
                    Label(fsuv2,text="Rs:- 22.53lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=4,column=2,padx=30)

                    Label(fsuv2,text="High & Comfort",fg="Black",relief='ridge',font="times 13 bold").grid(row=1,column=3,padx=30)
                    Label(fsuv2,text="Spacious & Premium Interior",fg="Black",relief='ridge',font="times 13 bold").grid(row=2,column=3,padx=30)
                    Label(fsuv2,text="Supreme Luxury",fg="Black",relief='ridge',font="times 13 bold").grid(row=3,column=3,padx=30)
                    Label(fsuv2,text="Absolute Power",fg="Black",relief='ridge',font="times 13 bold").grid(row=4,column=3,padx=30)
                   
                    Label(fsuv2,text="Model",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=0,padx=30)
                    Label(fsuv2,text="Ex-Showroom Price",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=2,padx=30)
                    Label(fsuv2,text="Specification",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=3,padx=30)
                    

                elif vrsuv.get()==2:
                    
                    fsuv3=Frame(rootsuv,bd=5,bg='Papaya Whip',height=5,relief=SUNKEN)
                    fsuv3.grid(row=1,column=2,padx=750)
                    

                    Label(fsuv3,text="1.6 Petrol E",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=1,column=0,padx=30)
                    Label(fsuv3,text="1.4 Petrol E Plus",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=2,column=0,padx=30)
                    Label(fsuv3,text="1.4 Diesel S",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=3,column=0,padx=30)
                    Label(fsuv3,text="1.6 Diesel SX Plus",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=4,column=0,padx=30)

                    Label(fsuv3,text="Rs:- 09.29 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=1,column=2,padx=30)
                    Label(fsuv3,text="Rs:- 10.00 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=2,column=2,padx=30)
                    Label(fsuv3,text="Rs:- 11.98 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=3,column=2,padx=30)
                    Label(fsuv3,text="Rs:- 12.22 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=4,column=2,padx=30)

                    Label(fsuv3,text="Sunroof High width 10mm",fg="Black",relief='ridge',font="times 13 bold").grid(row=1,column=3,padx=30)
                    Label(fsuv3,text="Spacious with 6 Airbags",fg="Black",relief='ridge',font="times 13 bold").grid(row=2,column=3,padx=30)
                    Label(fsuv3,text="intial 0-60 in 8.7secs auto",fg="Black",relief='ridge',font="times 13 bold").grid(row=3,column=3,padx=30)
                    Label(fsuv3,text="Amplified Power Adition With keyguards",fg="Black",relief='ridge',font="times 13 bold").grid(row=4,column=3,padx=30)
                   


                    
                    
                    Label(fsuv3,text="Model",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=0,padx=30)
                    Label(fsuv3,text="Ex-Showroom Price",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=2,padx=30)
                    Label(fsuv3,text="Specification",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=3,padx=30)


                elif vrsuv.get()==3:
                    
                    fsuv4=Frame(rootsuv,bd=5,bg='Plum',height=7,relief=SUNKEN)
                    fsuv4.grid(row=1,column=2,padx=750)
                    

                    Label(fsuv4,text="2WD Manual Diesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=1,column=0,padx=30)
                    Label(fsuv4,text="2WD AT Atomatic",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=2,column=0,padx=30)
                    Label(fsuv4,text="4WD AT Manual",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=3,column=0,padx=30)
                    Label(fsuv4,text="4WD AT Automatic",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=4,column=0,padx=30)

                    Label(fsuv4,text="Rs:- 32.61 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=1,column=2,padx=30)
                    Label(fsuv4,text="Rs:- 33.99 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=2,column=2,padx=30)
                    Label(fsuv4,text="Rs:- 35.34 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=3,column=2,padx=30)
                    Label(fsuv4,text="Rs:- 36.49 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=4,column=2,padx=30)

                    Label(fsuv4,text="High & Comfort",fg="Black",relief='ridge',font="times 13 bold").grid(row=1,column=3,padx=30)
                    Label(fsuv4,text="0-60 in 9.2Secs Interior",fg="Black",relief='ridge',font="times 13 bold").grid(row=2,column=3,padx=30)
                    Label(fsuv4,text="Luxury,sporty gear",fg="Black",relief='ridge',font="times 13 bold").grid(row=3,column=3,padx=30)
                    Label(fsuv4,text="Contrast Adition with anti fog lamps",fg="Black",relief='ridge',font="times 13 bold").grid(row=4,column=3,padx=30)
                    
                    Label(fsuv4,text="Model",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=0,padx=30)
                    Label(fsuv4,text="Ex-Showroom Price",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=2,padx=30)
                    Label(fsuv4,text="Specification",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=3,padx=30)
                     
                        

           
            def exitsuv():
            
                rootsuv.destroy()
            Button(fsuv1,text='EXIT',width=10,height=5,bg='Indian Red',bd=10,command=exitsuv).grid(row=10,column=0)
            Button(fsuv1,text="VIEW",width=10,height=5,bg='Blanched Almond',bd=10,command=viewsuv).grid(row=10,column=4)

           
                
        def sedan():
            
            rootsedan=Toplevel()
            rootsedan.configure(bg='Powder Blue')
            rootsedan.geometry("1600x800+0+0")
            rootsedan.title('SEDAN')
            fsedan1=Frame(rootsedan,width=1600,height=800,bd=20,bg='Light Steel Blue',relief=SUNKEN)
            fsedan1.pack(side=LEFT)

            Label(fsedan1,text="CHANGE YOUR APPROACH TO\n FINDING YOUR NEW SEDAN",font='arial 25',fg='Indian Red',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)

            vrsedan=IntVar()
            
            Radiobutton(fsedan1,text='Hyundai SONATA \n Undeniable Style.Pure SONATA',variable=vrsedan,value=1,font='times 20 bold').grid(row=3,column=3,padx=5,pady=5)
            Radiobutton(fsedan1,text='Hyundai ELANTRA \n Right Fit for Your Lifestyle.',variable=vrsedan,value=2,font='times 20 bold').grid(row=6,column=3,padx=5,pady=5)
            Radiobutton(fsedan1,text='Hyundai VERNA \n Intelligent by Design',variable=vrsedan,value=3,font='times 20 bold').grid(row=9,column=3,padx=5,pady=5)

            def viewsedan():

                if vrsedan.get()==1:
                        fsedan2=Frame(rootsedan,bd=5,bg='Light Steel Blue',height=6,relief=SUNKEN)
                        fsedan2.grid(row=1,column=2,padx=750)

                        Label(fsedan2,text="GOLD Manual Petrol",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=1,column=0,padx=30)
                        Label(fsedan2,text="2.7 V6 AT Petrol",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=2,column=0,padx=30)
                        Label(fsedan2,text="2.4 GDI MT Diesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=3,column=0,padx=30)
                        Label(fsedan2,text="2.4 GDI AT Diesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=4,column=0,padx=30)

                        Label(fsedan2,text="Rs:- 13.08 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=1,column=2,padx=30)
                        Label(fsedan2,text="Rs:- 15.99 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=2,column=2,padx=30)
                        Label(fsedan2,text="Rs:- 18.26 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=3,column=2,padx=30)
                        Label(fsedan2,text="Rs:- 20.53 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=4,column=2,padx=30)

                        Label(fsedan2,text="High & Comfort",fg="Black",relief='ridge',font="times 13 bold").grid(row=1,column=3,padx=30)
                        Label(fsedan2,text="3 Lever Soccer",fg="Black",relief='ridge',font="times 13 bold").grid(row=2,column=3,padx=30)
                        Label(fsedan2,text="Sunroof,6 Speed",fg="Black",relief='ridge',font="times 13 bold").grid(row=3,column=3,padx=30)
                        Label(fsedan2,text="S Line Style",fg="Black",relief='ridge',font="times 13 bold").grid(row=4,column=3,padx=30)
                       


                        
                        
                        Label(fsedan2,text="Model",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=0,padx=30)
                        Label(fsedan2,text="Ex-Showroom Price",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=2,padx=30)
                        Label(fsedan2,text="Specification",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=3,padx=30)
                
                elif vrsedan.get()==2:
                        fsedan3=Frame(rootsedan,bd=5,bg='Papaya Whip',height=6,relief=SUNKEN)
                        fsedan3.grid(row=1,column=2,padx=750)

                        Label(fsedan3,text="2.0 MPi S Petrol",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=1,column=0,padx=30)
                        Label(fsedan3,text="2.0 MPi SX Petrol",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=2,column=0,padx=30)
                        Label(fsedan3,text="2.0 SX(AT) Diesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=3,column=0,padx=30)
                        Label(fsedan3,text="2.0 SX(O) Diesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=4,column=0,padx=30)

                        Label(fsedan3,text="Rs:- 12.08 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=1,column=2,padx=30)
                        Label(fsedan3,text="Rs:- 14.99 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=2,column=2,padx=30)
                        Label(fsedan3,text="Rs:- 15.26 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=3,column=2,padx=30)
                        Label(fsedan3,text="Rs:- 16.53 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=4,column=2,padx=30)

                        Label(fsedan3,text="High M sport",fg="Black",relief='ridge',font="times 13 bold").grid(row=1,column=3,padx=30)
                        Label(fsedan3,text="Spacious & Child lock",fg="Black",relief='ridge',font="times 13 bold").grid(row=2,column=3,padx=30)
                        Label(fsedan3,text="ABS 2 Lever",fg="Black",relief='ridge',font="times 13 bold").grid(row=3,column=3,padx=30)
                        Label(fsedan3,text="Cruise control",fg="Black",relief='ridge',font="times 13 bold").grid(row=4,column=3,padx=30)
                        
                        Label(fsedan3,text="Model",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=0,padx=30)
                        Label(fsedan3,text="Ex-Showroom Price",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=2,padx=30)
                        Label(fsedan3,text="Specification",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=3,padx=30)



                elif vrsedan.get()==3:
                        fsedan4=Frame(rootsedan,bd=5,bg='PLUM',height=6,relief=SUNKEN)
                        fsedan4.grid(row=1,column=2,padx=750)

                        Label(fsedan4,text="CRDI 1.6 SX Petrol",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=1,column=0,padx=30)
                        Label(fsedan4,text="CRDi 1.6 AT SX Plus",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=2,column=0,padx=30)
                        Label(fsedan4,text="VTVT 1.6 E MD",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=3,column=0,padx=30)
                        Label(fsedan4,text="VTVT 1.6 E ATD",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=4,column=0,padx=30)

                        Label(fsedan4,text="Rs:- 12.08 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=1,column=2,padx=30)
                        Label(fsedan4,text="Rs:- 14.99 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=2,column=2,padx=30)
                        Label(fsedan4,text="Rs:- 15.26 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=3,column=2,padx=30)
                        Label(fsedan4,text="Rs:- 16.53 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=4,column=2,padx=30)

                        Label(fsedan4,text="High Front fog lamp",fg="Black",relief='ridge',font="times 13 bold").grid(row=1,column=3,padx=30)
                        Label(fsedan4,text="Isofix child seat",fg="Black",relief='ridge',font="times 13 bold").grid(row=2,column=3,padx=30)
                        Label(fsedan4,text="Supreme park sensor",fg="Black",relief='ridge',font="times 13 bold").grid(row=3,column=3,padx=30)
                        Label(fsedan4,text="Traction control",fg="Black",relief='ridge',font="times 13 bold").grid(row=4,column=3,padx=30)
                                               
                        Label(fsedan4,text="Model",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=0,padx=30)
                        Label(fsedan4,text="Ex-Showroom Price",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=2,padx=30)
                        Label(fsedan4,text="Specification",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=3,padx=30)



            
            def exitsedan():
                rootsedan.destroy()
            Button(fsedan1,text='EXIT',width=10,height=5,bg='Indian Red',bd=10,command=exitsedan).grid(row=10,column=0)
            Button(fsedan1,text="VIEW",width=10,height=5,bg='Blanched Almond',bd=10,command=viewsedan).grid(row=10,column=4)

        def hatchback():
            
            roothatchback=Toplevel()
            roothatchback.configure(bg='Beige')
            roothatchback.geometry("1600x800+0+0")
            roothatchback.title('HATCHBACK')
            fhatchback1=Frame(roothatchback,width=1600,height=800,bd=20,bg='Light Steel Blue',relief=SUNKEN)
            fhatchback1.pack(side=LEFT)

            Label(fhatchback1,text="CATCH THE 'i'",font='arial 25',fg='Indian Red',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)

            vrhatchback=IntVar()
            
            Radiobutton(fhatchback1,text='Elite i20 \n Live Premium',variable=vrhatchback,value=1,font='times 20 bold').grid(row=3,column=3,padx=5,pady=5)
            Radiobutton(fhatchback1,text='i20 Active \n Live Active',variable=vrhatchback,value=2,font='times 20 bold').grid(row=6,column=3,padx=5,pady=5)
            Radiobutton(fhatchback1,text='Grand i10 \n Its Wowsome!!',variable=vrhatchback,value=3,font='times 20 bold').grid(row=9,column=3,padx=5,pady=5)    


            def viewhatchback():
                if vrhatchback.get()==1:
                        fhatchback2=Frame(roothatchback,bd=5,bg='Light Steel Blue',height=6,relief=SUNKEN)
                        fhatchback2.grid(row=1,column=2,padx=750)

                        Label(fhatchback2,text="1.4 Sportz MD",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=1,column=0,padx=30)
                        Label(fhatchback2,text="1.2 ASTA MPetrol",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=2,column=0,padx=30)
                        Label(fhatchback2,text="1.4 ASTA O MDiesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=3,column=0,padx=30)
                        Label(fhatchback2,text="1.6 ASTA DualTone MD",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=4,column=0,padx=30)

                        Label(fhatchback2,text="Rs:- 07.68 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=1,column=2,padx=30)
                        Label(fhatchback2,text="Rs:- 07.99 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=2,column=2,padx=30)
                        Label(fhatchback2,text="Rs:- 08.26 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=3,column=2,padx=30)
                        Label(fhatchback2,text="Rs:- 08.53 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=4,column=2,padx=30)

                        Label(fhatchback2,text="High PAS Comfort",fg="Black",relief='ridge',font="times 13 bold").grid(row=1,column=3,padx=30)
                        Label(fhatchback2,text="Premium Heated Mirror",fg="Black",relief='ridge',font="times 13 bold").grid(row=2,column=3,padx=30)
                        Label(fhatchback2,text="Supreme Roof rails",fg="Black",relief='ridge',font="times 13 bold").grid(row=3,column=3,padx=30)
                        Label(fhatchback2,text="Absolute alloy Wheels",fg="Black",relief='ridge',font="times 13 bold").grid(row=4,column=3,padx=30)
                       

                        Label(fhatchback2,text="Model",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=0,padx=30)
                        Label(fhatchback2,text="Ex-Showroom Price",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=2,padx=30)
                        Label(fhatchback2,text="Specification",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=3,padx=30)



                elif vrhatchback.get()==2:
                        fhatchback3=Frame(roothatchback,bd=5,bg='Papaya Whip',height=6,relief=SUNKEN)
                        fhatchback3.grid(row=1,column=2,padx=750)

                        Label(fhatchback3,text="1.2 SX DT MD",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=1,column=0,padx=30)
                        Label(fhatchback3,text="1.4 SX AVN MD",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=2,column=0,padx=30)
                        Label(fhatchback3,text="1.4 MP MT Diesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=3,column=0,padx=30)
                        Label(fhatchback3,text="1.4 MP AT Diesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=4,column=0,padx=30)

                        Label(fhatchback3,text="Rs:- 06.88 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=1,column=2,padx=30)
                        Label(fhatchback3,text="Rs:- 07.99 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=2,column=2,padx=30)
                        Label(fhatchback3,text="Rs:- 08.26 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=3,column=2,padx=30)
                        Label(fhatchback3,text="Rs:- 09.88 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=4,column=2,padx=30)

                        Label(fhatchback3,text="Central Window",fg="Black",relief='ridge',font="times 13 bold").grid(row=1,column=3,padx=30)
                        Label(fhatchback3,text="Spacious & Premium Interior",fg="Black",relief='ridge',font="times 13 bold").grid(row=2,column=3,padx=30)
                        Label(fhatchback3,text="Supreme Steering",fg="Black",relief='ridge',font="times 13 bold").grid(row=3,column=3,padx=30)
                        Label(fhatchback3,text="ABS Powerbreak",fg="Black",relief='ridge',font="times 13 bold").grid(row=4,column=3,padx=30)
                       

                        Label(fhatchback3,text="Model",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=0,padx=30)
                        Label(fhatchback3,text="Ex-Showroom Price",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=2,padx=30)
                        Label(fhatchback3,text="Specification",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=3,padx=30)


                elif vrhatchback.get()==3:
                        fhatchback4=Frame(roothatchback,bd=5,bg='plum',height=6,relief=SUNKEN)
                        fhatchback4.grid(row=1,column=2,padx=750)

                        Label(fhatchback4,text="1.2 ERA KAPPA MPTR",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=1,column=0,padx=30)
                        Label(fhatchback4,text="1.2 KAPPA MAGNA PTR",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=2,column=0,padx=30)
                        Label(fhatchback4,text="1.2 KAPPA Sportz MPTR",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=3,column=0,padx=30)
                        Label(fhatchback4,text="1.2 CRDI AT Diesel",fg="royal blue",relief='ridge',font="times 13 bold").grid(row=4,column=0,padx=30)

                        Label(fhatchback4,text="Rs:- 05.08 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=1,column=2,padx=30)
                        Label(fhatchback4,text="Rs:- 05.99 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=2,column=2,padx=30)
                        Label(fhatchback4,text="Rs:- 06.26 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=3,column=2,padx=30)
                        Label(fhatchback4,text="Rs:- 06.53 lakh",fg="Maroon",relief='ridge',font="times 13 bold").grid(row=4,column=2,padx=30)

                        Label(fhatchback4,text="High & Comfort",fg="Black",relief='ridge',font="times 13 bold").grid(row=1,column=3,padx=30)
                        Label(fhatchback4,text="Alarm,Audio Remote",fg="Black",relief='ridge',font="times 13 bold").grid(row=2,column=3,padx=30)
                        Label(fhatchback4,text="Supreme Locking",fg="Black",relief='ridge',font="times 13 bold").grid(row=3,column=3,padx=30)
                        Label(fhatchback4,text="Absolute Control",fg="Black",relief='ridge',font="times 13 bold").grid(row=4,column=3,padx=30)
                       

                        Label(fhatchback4,text="Model",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=0,padx=30)
                        Label(fhatchback4,text="Ex-Showroom Price",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=2,padx=30)
                        Label(fhatchback4,text="Specification",font="times 15 bold",fg="Black",relief='ridge').grid(row=0,column=3,padx=30)


                
            def exithatchback():
                roothatchback.destroy()
            Button(fhatchback1,text='EXIT',width=10,height=5,bg='Indian Red',bd=10,command=exithatchback).grid(row=10,column=0)
            Button(fhatchback1,text="VIEW",width=10,height=5,bg='Blanched Almond',bd=10,command=viewhatchback).grid(row=10,column=4)

        def showlist():
            show=Tk()
            show.configure(bg='Light Steel Blue')
            Label(show,text="Booking_ID   Customer _Name   Customer_UID    Car_Name    Booking_Amount   Exp_Delivery_Date   Payment_Mode",font='times 20').pack()
            con=sqlite3.Connection('book')
            cur=con.cursor()
            cur.execute('select * from bookings')
            con.commit()
            a=cur.fetchall()
            j=0
            while j<len(a):
                b=[str( i[0]) for i in a]
                b=str(b[j])
                c=[str( i[1]) for i in a]
                c=str(c[j])
                d=[str( i[2]) for i in a]
                d=str(d[j])
                e=[str( i[3]) for i in a]
                e=str(e[j])
                f=[str( i[4]) for i in a]
                f=str(f[j])
                g=[str( i[5]) for i in a]
                g=str(g[j])
                h=[str( i[6]) for i in a]
                h=str(h[j])
                Label(show,text=b+'              '+c+'                 '+d+'                    '+e+'               '+f+'                '+g+'              '+h,bg='Light Steel Blue',font='times 18').pack()
                j=j+1 
 

        def booking():
            def book():
                if bk1.get()=='' or bk2.get()=='':
                    showerror("Invalid Entry","Entry valid details")
                if int(bk4.get()) <50000:
                    showerror("Invalid Amount","Minimum amount for booking is: 50000")
                else:
                    print var.get()
                    d=str(random.randint(1,28))+"/"+str(random.randint(1,12))+"/"+str(random.randint(2018,2019))
                    con=sqlite3.Connection('book')
                    cur=con.cursor()
                    cur.execute('create table if not exists bookings(bookid number(10),cust_name varchar(20),cust_uid varchar(10),car_name varchar(20),booking_amt number(7),delivery_date varchar(9),Mode_of_payment varchar(20))')
                    a=[(bid,bk1.get(),bk2.get(),var.get(),bk4.get(),d,var1.get() )]
                    print var1.get()
                    cur.executemany('insert into bookings values(?,?,?,?,?,?,?)',a)
                    con.commit()
                    cur.execute('select * from bookings')
                    a=cur.fetchall()
                    print a
                    showinfo("Congratulations!!","You have successfully booked your car \n Your expected delivery date is"+d) 
            
            rootbook=Toplevel()
            rootbook.configure(bg='Beige')
            rootbook.geometry("1600x800+0+0")
            rootbook.title('BOOKING')
            fbook1=Frame(rootbook,width=1600,height=800,bd=20,bg='Light Steel Blue',relief=SUNKEN)
            fbook1.pack(side=LEFT)

            Label(fbook1,text="BOOK HERE",font='arial 25',fg='Indian Red',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)   #HEAD

            Label(fbook1,text="Booking Id:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=1,column=1,sticky='W')

            Label(fbook1,text="Customer's Name:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=2,column=1,sticky='W')
            bk1=Entry(fbook1,width=16,bd=5,font='arial 20')
            bk1.grid(row=2,column=3)

            Label(fbook1,text="Customer's UID:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=3,column=1,sticky='W')
            bk2=Entry(fbook1,width=16,bd=5,font='arial 20')
            bk2.grid(row=3,column=3)

            Label(fbook1,text="Car Name:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=4,column=1,sticky='W')

            Options=["TUCSON 2WD MT","TUCSON 2WD AT GL","TUCSON 2WD MT","TUCSON AT GL" "CRETA 1.6 E","CRETA 1.4 E PLUS","CRETA 1.4 S","CRETA 1.6 SX PLUS" "SantaFE 2WD MD","SantaFE 2WD AT AUTO","SantaFE 4 WDAT MANUAL","SantaFE 4WD AT","SONATA GOLD","SONATA 2.7 V6 AT","VERNA 2.4 GDI MT","VERNA 2.4 GDI MT","ELANTRA 2.0 MPI S","ELANTRA 2.0 MPI SX","ELANTRA 2.0 SX(AT)","ELANTRA 2.0 SX(O)","Elite i20","i20 Active","Grand i10"]   ##ENter the names of all the cars.....Add names of the cars and adjust the size of the drop down
            var = StringVar()
            var.set("Hyundai")
            DropDownMenu=apply(OptionMenu, (fbook1, var) + tuple(Options))
            DropDownMenu.grid(row=4,column=3)
       
                
            Label(fbook1,text="Booking Amount:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=5,column=1,sticky='W')
            bk4=Entry(fbook1,width=16,bd=5,font='arial 20')
            bk4.grid(row=5,column=3)

            bid=random.randint(1000,5698)

            Label(fbook1,text="Expected Delivery:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=6,column=1,sticky='W')

            Label(fbook1,text="Mode of Payment:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=7,column=1,sticky='W')
            
            Option=["Card","Cash","DD","NEFT","Net_Banking"]
            var1 = StringVar()
            var1.set("Select Mode")
            DropDownMenu=apply(OptionMenu, (fbook1, var1) + tuple(Option))
            DropDownMenu.grid(row=7,column=3)
       

            def exitbook():
                rootbook.destroy()
            Button(fbook1,text='EXIT',font='times 20 bold',width=10,height=2,bd=10,bg='Indian Red',command=exitbook).grid(row=8,column=2)

            Button(fbook1,text='BOOK',font='times 20 bold',width=10,height=2,bd=10,bg='Pale Goldenrod',command=book).grid(row=8,column=4)

        def exitmain():
            root.destroy()
        Button(fm1,text='EXIT',font='times 20 bold',width=13,height=2,bd=10,bg='Indian Red',command=exitmain).grid(row=6,column=3)

        Button(fm1,text='SUV',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=suv).grid(row=2,column=3)

        Button(fm1,text='SEDAN',font='times 20 bold',width=13,height=2,bd=10,bg='Powder Blue',command=sedan).grid(row=3,column=2,pady=50)

        Button(fm1,text='HATCHBACK',font='times 20 bold',width=13,height=2,bd=10,bg='Beige',command=hatchback).grid(row=3,column=5,pady=50)

        Button(fm1,text='BOOK NOW',font='times 20 bold',width=13,height=2,bd=10,bg='Pale Goldenrod',command=booking).grid(row=5,column=5)

        Button(fm1,text='BOOKING LIST',font='times 20 bold',width=13,height=2,bd=10,bg='Pale Goldenrod',command=showlist).grid(row=5,column=2,pady=15)


    else:
         showerror('!OOPS','Invalid Username or Password')    
         
def close():
    admin.destroy()

Button(admin,text="EXIT",command=close,width=5,height=2,bd=5,bg='Indian Red').grid(row=9,column=2)
Button(admin,text="LOGIN",command=login,width=5,height=2,bd=5,bg='Plum').grid(row=9,column=4)

admin.mainloop()




