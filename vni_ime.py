import sublime, sublime_plugin

_STATUS = False
_MOD = False 
_LAST_KEY = ''
class SaveOnModifiedListener(sublime_plugin.EventListener):
    def on_modified(self, view):
        global _STATUS
        global _MOD
        if not _STATUS:
            return
        if not _MOD:
            view.run_command('startime')
        _MOD = False
class StartimeCommand(sublime_plugin.TextCommand): 
    curPost = 0
    curSize = 0
    stateIME = True
    keyDefine = ['1','2','3','4','5','6','7','8','9','0']
    def run(self, edit):
        pos = self.view.sel()[0] 
        global _LAST_KEY
        if self.view.size() > self.curSize : 
            a = pos.begin() - 1
            b = pos.end()   
            charRegion = sublime.Region(a, b)
            char = self.view.substr(charRegion)
            if self.find_key_unicode(char):
                if self.check_grammar(self.view.word(charRegion)):
                    final = self.replace_word_key(char,self.view.word(charRegion))
                    if final :
                        global _MOD
                        self.view.run_command("runchange", {'a':a,'b':b,"final":final})  
                        _MOD = True
            self.curPost = pos                 
            self.curSize = self.view.size();
            _LAST_KEY = char
        elif self.view.size() < self.curSize:
            self.curSize = self.view.size();
        
    def find_key_unicode(self,key):
        if key in self.keyDefine: 
            return True
        return False  
    def check_grammar(self,word):
        word = self.view.substr(word)   
        # _len = len(word)-2
        # for i in _len:
        #   if word[i] == word[i+1]: 
        #       return False
        return True 

    def replace_word_key(self,key,word):
        word = self.view.substr(word)
        finalWord = '' 
        charSour = ''
        charDest = ''
        if key == '1':
            charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                        'á','í','é','ó','ý','ú',
                        'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                        'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                        'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                        'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử']
            charDest = ['á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                        'a','i','e','o','y','u',
                        'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                        'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                        'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                        'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',]
        elif key == '2':
            charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                        'ì','à','è','ì','ò','ỳ',
                        'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                        'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                        'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                        'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử']
            charDest = ['à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                        'i','a','e','i','o','y',
                        'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                        'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                        'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                        'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ']
        elif key == '3':
            charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                        'ỏ','ả','ẻ','ỉ','ỏ','ỷ','ủ',
                        'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                        'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                        'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                        'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',]
            charDest = ['ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                        'o','a','e','i','o','y','u',
                        'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                        'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                        'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                        'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử']

        elif key == '4':
            charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                        'ẽ','ã','ẽ','ĩ','õ','ỹ','ũ'
                        'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                        'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                        'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                        'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử']
            charDest = ['ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                        'e','a','e','i','o','y','u'
                        'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                        'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                        'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                        'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ']
        elif key == '5':
            charSour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                        'ạ','ẹ','ị','ọ','ụ',
                        'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                        'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                        'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                        'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử']
            charDest = ['ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                        'a','e','i','o','u',
                        'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                        'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                        'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                        'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự']
        elif key == '6':
            charSour = ['a','e','â','ê','o']
            charDest = ['â','ê','a','e','ô']    
        elif key == '7':
            charSour = ['u','o','ư','ơ']
            charDest = ['ư','ơ','u','o']
        elif key == '8':
            charSour = ['a','ă']
            charDest = ['ă','a']
        elif key == '9':
            charSour = ['d','đ','D','Đ']
            charDest = ['đ','d','Đ','D']
        elif key == '0':
            charSour = ['à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                        'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                        'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                        'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                        'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ']
            charDest = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                        'a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                        'a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                        'a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                        'a','ă','â','e','ê','i','o','ơ','ô','y','u','ư']
        finalWord = self.convertWordChar(key,word,charSour,charDest)
        if finalWord != word:   
            return finalWord
        return False
    def convertWordChar(self,key,word,charSour,charDest):
        global _LAST_KEY
        _list_word = list(word)
        _list_consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
        _list_exception_character_of_vietnamese = ['ơ','ớ','ờ',
                                                   'ở','ỡ','ợ',
                                                   'e','é','è',
                                                   'ẻ','ẽ','ẹ',
                                                   'ê','ế','ề',
                                                   'ể','ễ','ệ']
        _index_first_vowel = -1
        _index_exception = -1
        _count_vowel = 0
        _index_changed_character = -1
        _has_changed = False
        preKey = ''
        _debug = ''
        del _list_word[-1]
        if len(_list_word) > 0:
            preKey = _list_word[-1]
        if len(_list_word) > 7 or (len(_list_word) >2 and _list_word[0] in ['o','e'] ):
            return word
        
        for i in range(len(_list_word)):
            for j in range(len(_list_consonant)):
                if _list_word[i] == _list_consonant[j]:
                    break
                elif j == len(_list_consonant)-1:
                    if _list_word[i] in _list_exception_character_of_vietnamese:
                        _index_exception = i
                    if _index_first_vowel == -1:
                        _index_first_vowel = i
                    _count_vowel += 1

        if _index_exception != -1:
            _index_changed_character = _index_exception
            if key == '7' and _index_first_vowel + _count_vowel < len(_list_word):
                for i in range(len(charSour)):
                    if _list_word[_index_changed_character-1] == charSour[i]:
                        _list_word[_index_changed_character-1] = charDest[i]
                        break
        elif _count_vowel == 3:
            _index_changed_character = _index_first_vowel+1
            if key == '7':
                for i in range(len(charSour)):
                    if _list_word[_index_changed_character-1] == charSour[i]:
                        _list_word[_index_changed_character-1] = charDest[i]
                        break
        elif _count_vowel == 2:
            if _index_first_vowel + _count_vowel < len(_list_word):
                _index_changed_character = _index_first_vowel+1
                if key == '7':
                    for i in range(len(charSour)):
                        if _list_word[_index_changed_character-1] == charSour[i]:
                            _list_word[_index_changed_character-1] = charDest[i]
                            break
            else:
                if key == '7':
                    _index_changed_character = _index_first_vowel+1
                else:
                    _index_changed_character = _index_first_vowel
        elif _count_vowel == 1:
            _index_changed_character = _index_first_vowel
        elif key == '9':
            _index_changed_character = 0
        
        for i in range(len(charSour)):
            if _list_word[_index_changed_character] == charSour[i]:
                _list_word[_index_changed_character] = charDest[i]
                _has_changed = True
                break

        if _LAST_KEY == key:
            if preKey != key:
                _list_word.append(_LAST_KEY)
        if _has_changed :
            word = "".join(_list_word) 
        return word
class ControlimeCommand(sublime_plugin.TextCommand):
    stateIME = True
    def run(self, edit):
        global _STATUS
        if self.stateIME == False:
            _STATUS = False
            self.stateIME = True        
            sublime.status_message("VN IME Stoped")
            self.view.set_status('VN IME'," VN IME : OFF")
        elif self.stateIME :
            _STATUS = True   
            self.stateIME = False
            sublime.status_message("VN IME Started")
            self.view.set_status('VN IME'," VN IME : ON")

class RunchangeCommand(sublime_plugin.TextCommand):
    def run(self, edit, a, b, final):
        charRegion = sublime.Region(a, b)
        self.view.replace(edit,self.view.word(charRegion),final)