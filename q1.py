attended_utsava = {'adarsh','simha','mithun','anil'}
attended_maya = {'darshan','arun','adarsh','mithun'}

attended_both = attended_utsava&attended_maya
print(f'People who attended both are  {attended_both}')

attended_one  = attended_utsava^attended_maya
print(f'People who attended one among maya or utsava are {attended_one}')

attending_atleast_one = attended_maya|attended_utsava
print(f'People who are attending atleast one among maya or utsava are {attending_atleast_one}')
