import telebot
import pickle
import re
import random
import datetime
import os
import math

import const
bot = telebot.TeleBot('818916051:AAE5fi1XFmwuB_cQ8H6RHGvnJ28_zDNKVV4')
print(bot.get_me())





@bot.message_handler(commands=['close_mega'])
def start(message):
	
    if(message.from_user.id in const.admins):
        
        
         
        
        #выше запоминаем айди закрытия
        
        
        bot.send_message(message.chat.id, const.setings['Закрытие'])
        
@bot.message_handler(commands=['open_mega'])
def start(message):
    if(message.from_user.id in const.admins):
        
# выше запоминаем айди открытия        
       
        bot.send_message(message.chat.id, const.setings['Открытие'])
       
        bot.pin_chat_message(message.chat.id, message.message_id +1)


@bot.message_handler(commands=['open'])
def start(message):
    if(message.from_user.id in const.admins):
        const.setings['open_id'] = message.message_id
        
# выше запоминаем айди открытия        
       
        bot.send_message(message.chat.id, const.setings['Открытие'])
       
        bot.pin_chat_message(message.chat.id, message.message_id +1)
        try:
        	for ty in const.autt:
        		bot.send_message(message.chat.id, '{a}'.format(a = ty))
        except:
        	pass
        
  			
        		
        
        		
        	
    
    	
    		

#ответ на команду close

@bot.message_handler(commands=['close'])
def start(message):
	
    if(message.from_user.id in const.admins):
        const.megaac = []
        const.setings['close_id'] = message.message_id
        

        
        #выше запоминаем айди закрытия
        
        
        bot.send_message(message.chat.id, const.setings['Закрытие'])
        


        
        for d in range(const.setings['open_id'], const.setings['close_id']): #чекаем айди и начинаем форвард сообщений
        
        
            try:
                mes = bot.forward_message(-1001469250576, message.chat.id, d)
            except telebot.apihelper.ApiException:
                pass
            if (mes.text != ''):
                if (mes.content_type == 'text'):
                	acmeg = re.findall(r'\[.+\]\(.+?\.me/.+?\)', mes.text)
                	for ms in acmeg:
                		if ms not in const.megaac:
                			const.megaac.append(ms)
                			
          
            	
            			
        else:
        	
        	
            f = const.setings['Гиф_меги'] + const.setings['Заголовок'] + "\n" + "\n"+ const.ch + "\n" + "\n"
            for innt in const.megaac:
            
                f = f  + str(innt)  + "\n"
            else:
                bot.send_message(message.chat.id, f + "\n" + "\n" + const.ch + "\n" + '\n' + const.setings['Окончание'] + "\n", parse_mode='Markdown')

                		
                
                                                
#сообщение готовности
                
                bot.send_message(message.chat.id, const.setings['Готовность'], parse_mode='Markdown')
                                    


  
bot.polling(none_stop = True)  
  
