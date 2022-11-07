from django import forms
from .models import history



#class TransactionForm(forms.ModelForm):
 #  class Meta:
   #        model= history
     #      fields=['qid','status','update_time']
        #   widgets={
           #  'transaction_id' :forms.TextInput(attrs={'class' : 'form-control'}),
          #      'status':forms.TextInput(attrs={'class' : 'form-control'}),
             # 'update_time':forms.DateInput(attrs={'class' : 'form-control'}),

           # }