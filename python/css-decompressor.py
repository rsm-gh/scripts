#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#

#  Copyright (C) 2015-2016 Rafael Senties Martinelli
#
#  This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License 3 as published by
#   the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA.


__version__ = '1.4~0'


def inside_brackets(start, end, text):
    for i in range(start, end):
        if text[i]=='}':
            return True
        elif text[i]=='{':
            return False
            
    return False
    
def decompress_css(text):
    
    for char in ('\t','\n'):
        text=text.replace(char,'')

    indent_level=0
    new_text=''
    text_lenght=len(text)

    for i, char in enumerate(text):
        
        chars={k:'' for k in range(-4,4)}
        new_text_last_char=new_text[-1:]
        
        
        for k in range(-4,4):
            try:
                chars[k]=text[i+k]
            except:
                pass
        
        
        
        if  not new_text_last_char in (' ',':') and (
            (char in (',','%','>') and not chars[1] in (';',' ')) and \
            (new_text_last_char in (' ',':')) or \
            (char == 's' and chars[-1].isdigit() and not chars[1]+chars[2]=='ol') or \
            (char == ':' and not chars[1] == ' ' and inside_brackets(i, text_lenght, text)) or \
            (char in ('n','x') and chars[-4].isdigit() and ''.join(chars[x] for x in range(-3,1)) in ('vmin','vmax')) or \
            (char == 'm' and chars[-3].isdigit() and ''.join(chars[x] for x in range(-2,1)) == 'rem') or \
            (char == ')' and not chars[1] in (' ',';')) or \
            (char in ('m','x','n','t','c','h','v') and not chars[-3]==' ' and chars[-2].isdigit() \
                and chars[-1]+char in ('em','ex','px','cm','mm','in','pt','pc','ch','vh','vw') and chars[1] != ';')
                ):
        
            char+=' '
        
        
        elif not new_text_last_char in (' ',':') and (\
                (char == '#' and chars[-1] == ':') or \
                (char == '.' and not chars[-1].isdigit() and chars[1].isdigit()) or \
                (char == '!' and ''.join(chars[x] for x in range(1,4)) == 'imp')
                ):
        
                char = ' '+char
    
    
        elif char == ',':
            char = ', '
    
        elif char == '>':
            char = ' > '
    
        elif char == '{':
            
            indent_level+=1
            
            if new_text_last_char != ' ':
                char =' {\n'+'\t'*indent_level
            else:
                char ='{\n'+'\t'*indent_level
            
            
        elif char == '}':
            
            indent_level-=1
            char ='\n'+'\t'*indent_level+'}'
            if chars[1] != '}':
                char+='\n'+'\t'*indent_level
            
            if indent_level==0:
                char+='\n'
            
        elif char == ';':
            char = ';\n'+'\t'*indent_level
            
        new_text+=char
        
    return new_text
    

if __name__ == '__main__':
    

    with open('test.css') as f:
		print decompress_css(f.read())  

