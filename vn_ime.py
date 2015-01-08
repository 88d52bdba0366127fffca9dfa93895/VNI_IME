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
  _cur_post = 0
  _cur_size = 0
  _state_IME = True
  _key_define = ['1','2','3','4','5','6','7','8','9','0']

  def run(self, edit):
    _pos = self.view.sel()[0]
    global _LAST_KEY
    if self.view.size() > self._cur_size :
      _a = _pos.begin() - 1
      _b = _pos.end()
      _char_region = sublime.Region(_a, _b)
      _char = self.view.substr(_char_region)
      if self._find_key_unicode(_char):
        _final = self._replace_word_key(_char,self.view.word(_char_region))
        if _final :
          global _MOD
          self.view.run_command("runchange", {'_a':_a,'_b':_b,"_final":_final})
          _MOD = True
      self._cur_post = _pos
      self._cur_size = self.view.size();
      _LAST_KEY = _char
    elif self.view.size() < self._cur_size:
      self._cur_size = self.view.size();
    
  def _find_key_unicode(self,_key):
    if _key in self._key_define:
      return True
    return False

  def _is_vietnamese(self,_index_current_vowel,
                     _index_first_vowel,_count_vowel):
    if int(_index_current_vowel) == \
       int(_index_first_vowel) + int(_count_vowel) - 1:
      return True
    return False

  def _is_vietnamese_old_word(self,_list_word,_count_vowel):
    if _list_word[1] in ['i','I'] and _list_word[0] in ['g','G']:
      return True
    if _list_word[1] in ['u','U'] and _list_word[0] in ['q','Q']:
      return True
    return False

  def _is_english(self,_current_consonant,_count_vowel):
    _list_consonant_not_in_vietnamese = ['b','d','đ','f','j','k','l',
                                         'q','r','s','v','w','x','z',
                                         'B','D','Đ','F','J','K','L',
                                         'Q','R','S','V','W','X','Z']
    if _count_vowel != 0 and \
       _current_consonant in _list_consonant_not_in_vietnamese:
      return True
    return False

  def _replace_word_key(self,_key,_word):
    _word = self.view.substr(_word)
    _final_word = '' 
    _list_char_sour = ''
    _list_char_dest = ''

    if _key == '1':
      _list_char_sour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử',
                         'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự']
      _list_char_dest = ['á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ']
    elif _key == '2':
      _list_char_sour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử',
                         'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự']
      _list_char_dest = ['à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ']
    elif _key == '3':
      _list_char_sour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử',
                         'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự']
      _list_char_dest = ['ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử']
    elif _key == '4':
      _list_char_sour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử',
                         'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự']
      _list_char_dest = ['ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ',
                         'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ',
                         'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ',
                         'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư',
                         'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ']
    elif _key == '5':
      _list_char_sour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử'
                 'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự']
      _list_char_dest = ['ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư']
    elif _key == '6':
      _list_char_sour = ['a','á','à','ả','ã','ạ',
                         'ắ','ắ','ằ','ẳ','ẵ','ặ',
                         'â','ấ','ầ','ẩ','ẫ','ậ',
                         'e','é','è','ẻ','ẽ','ẹ',
                         'ê','ế','ề','ể','ễ','ệ',
                         'o','ó','ò','ỏ','õ','ọ',
                         'ô','ố','ồ','ổ','ỗ','ộ',
                         'A','Á','À','Ả','Ã','Ạ',
                         'Ắ','Ắ','Ằ','Ẳ','Ẵ','Ặ',
                         'Â','Ấ','Ầ','Ẩ','Ẫ','Ậ',
                         'E','É','È','Ẻ','Ẽ','Ẹ',
                         'Ê','Ế','Ề','Ể','Ễ','Ệ',
                         'O','Ó','Ò','Ỏ','Õ','Ọ',
                         'Ô','Ố','Ồ','Ổ','Ỗ','Ộ']
      _list_char_dest = ['â','ấ','ầ','ẩ','ẫ','ậ',
                         'â','ấ','ầ','ẩ','ẫ','ậ',
                         'a','á','à','ả','ã','ạ',
                         'ê','ế','ề','ể','ễ','ệ',
                         'e','é','è','ẻ','ẽ','ẹ',
                         'ô','ố','ồ','ổ','ỗ','ộ',
                         'o','ó','ò','ỏ','õ','ọ',
                         'Â','Ấ','Ầ','Ẩ','Ẫ','Ậ',
                         'Â','Ấ','Ầ','Ẩ','Ẫ','Ậ',
                         'A','Á','À','Ả','Ã','Ạ',
                         'Ê','Ế','Ề','Ể','Ễ','Ệ',
                         'E','É','È','Ẻ','Ẽ','Ẹ',
                         'Ô','Ố','Ồ','Ổ','Ỗ','Ộ',
                         'O','Ó','Ò','Ỏ','Õ','Ọ']
    elif _key == '7':
      _list_char_sour = ['o','ó','ò','ỏ','õ','ọ',
                         'ơ','ớ','ờ','ở','ỡ','ợ',
                         'u','ú','ù','ủ','ũ','ụ',
                         'ư','ứ','ừ','ử','ữ','ự',
                         'O','Ó','Ò','Ỏ','Õ','Ọ',
                         'Ơ','Ớ','Ờ','Ở','Ỡ','Ợ',
                         'U','Ú','Ù','Ủ','Ũ','Ụ',
                         'Ư','Ứ','Ừ','Ử','Ữ','Ự']
      _list_char_dest = ['ơ','ớ','ờ','ở','ỡ','ợ',
                         'o','ó','ò','ỏ','õ','ọ',
                         'ư','ứ','ừ','ử','ữ','ự',
                         'u','ú','ù','ủ','ũ','ụ',
                         'Ơ','Ớ','Ờ','Ở','Ỡ','Ợ',
                         'O','Ó','Ò','Ỏ','Õ','Ọ',
                         'Ư','Ứ','Ừ','Ử','Ữ','Ự',
                         'U','Ú','Ù','Ủ','Ũ','Ụ']
    elif _key == '8':
      _list_char_sour = ['a','á','à','ả','ã','ạ',
                         'ắ','ắ','ằ','ẳ','ẵ','ặ',
                         'A','Á','À','Ả','Ã','Ạ',
                         'Ắ','Ắ','Ằ','Ẳ','Ẵ','Ặ']
      _list_char_dest = ['ắ','ắ','ằ','ẳ','ẵ','ặ',
                         'a','á','à','ả','ã','ạ',
                         'Ắ','Ắ','Ằ','Ẳ','Ẵ','Ặ',
                         'A','Á','À','Ả','Ã','Ạ']
    elif _key == '9':
      _list_char_sour = ['d','đ','D','Đ']
      _list_char_dest = ['đ','d','Đ','D']
    elif _key == '0':
      _list_char_sour = ['a','ă','â','e','ê','i','o','ơ','ô','y','u','ư',
                         'á','ắ','ấ','é','ế','í','ó','ớ','ố','ý','ú','ứ',
                         'à','ằ','ầ','è','ề','ì','ò','ờ','ồ','ỳ','ù','ừ',
                         'ả','ẳ','ẩ','ẻ','ể','ỉ','ỏ','ở','ổ','ỷ','ủ','ử',
                         'ã','ẵ','ẫ','ẽ','ễ','ĩ','õ','ỡ','ỗ','ỹ','ũ','ữ',
                         'ạ','ặ','ậ','ẹ','ệ','ị','ọ','ợ','ộ','ỵ','ụ','ự',
                         'A','Ă','Â','E','Ê','I','O','Ơ','Ô','Y','U','Ư',
                         'Á','Ắ','Ấ','É','Ế','Í','Ó','Ớ','Ố','Ý','Ú','Ứ',
                         'À','Ằ','Ầ','È','Ề','Ì','Ò','Ờ','Ồ','Ỳ','Ù','Ừ',
                         'Ả','Ẳ','Ẩ','Ẻ','Ể','Ỉ','Ỏ','Ở','Ổ','Ỷ','Ủ','Ử',
                         'Ã','Ẵ','Ẫ','Ẽ','Ễ','Ĩ','Õ','Ỡ','Ỗ','Ỹ','Ũ','Ữ',
                         'Ạ','Ặ','Ậ','Ẹ','Ệ','Ị','Ọ','Ợ','Ộ','Ỵ','Ụ','Ự']
      _list_char_dest = ['a','a','a','e','e','i','o','o','o','y','u','u',
                         'a','a','a','e','e','i','o','o','o','y','u','u',
                         'a','a','a','e','e','i','o','o','o','y','u','u',
                         'a','a','a','e','e','i','o','o','o','y','u','u',
                         'a','a','a','e','e','i','o','o','o','y','u','u',
                         'a','a','a','e','e','i','o','o','o','y','u','u',
                         'A','A','A','E','E','I','O','O','O','Y','U','U',
                         'A','A','A','E','E','I','O','O','O','Y','U','U',
                         'A','A','A','E','E','I','O','O','O','Y','U','U',
                         'A','A','A','E','E','I','O','O','O','Y','U','U',
                         'A','A','A','E','E','I','O','O','O','Y','U','U',
                         'A','A','A','E','E','I','O','O','O','Y','U','U']

    _final_word = self._convert_word_char(_key,_word,_list_char_sour,_list_char_dest)
    if _final_word != _word:
      return _final_word
    return False

  def _convert_word_char(self,_key,_word,_list_char_sour,_list_char_dest):
    global _LAST_KEY
    _list_word = list(_word)
    _list_consonant = ['b','c','d','đ','f','g','h','j','k','l','m',
                       'n','p','q','r','s','t','v','w','x','z',
                       'B','C','D','Đ','F','G','H','J','K','L','M',
                       'N','P','Q','R','S','T','V','W','X','Z']
    _list_exception_character_of_vietnamese = [#'o','ó','ò',
                                               #'ỏ','õ','ọ',
                                               'ơ','ớ','ờ',
                                               'ở','ỡ','ợ',
                                               'ê','ế','ề',
                                               'ể','ễ','ệ',
                                               'Ơ','Ớ','Ờ',
                                               'Ở','Ỡ','Ợ',
                                               'Ê','Ế','Ề',
                                               'Ể','Ễ','Ệ']
    _index_first_vowel = -1
    _index_current_vowel = -1
    _current_consonant = ''
    _index_exception = -1
    _index_changed_character = -1
    _count_vowel = 0
    _has_changed = False
    _pre_key = ''
    _debug = ''
    
    del _list_word[-1]

    if len(_list_word) > 0:
      _pre_key = _list_word[-1]
    if len(_list_word) > 7:
      return word
    
    for i in range(len(_list_word)):
      for j in range(len(_list_consonant)):
        if _list_word[i] == _list_consonant[j]:
          _current_consonant = _list_word[i]
          if self._is_english(_current_consonant,_count_vowel):
            return word
          break
        elif j == len(_list_consonant)-1:
          _index_current_vowel = i
          if _list_word[i] in _list_exception_character_of_vietnamese:
            _index_exception = i
          if _index_first_vowel == -1:
            _index_first_vowel = i
          _count_vowel += 1
          if not self._is_vietnamese(_index_current_vowel,_index_first_vowel,_count_vowel):
            return word

    if _count_vowel > 1:
      if self._is_vietnamese_old_word(_list_word,_count_vowel):
        _index_first_vowel += 1
        _count_vowel -= 1

    if _index_exception != -1:
      _index_changed_character = _index_exception
      if _key == '7' and _index_first_vowel + _count_vowel < len(_list_word):
        for i in range(len(_list_char_sour)):
          if _list_word[_index_changed_character - 1] == _list_char_sour[i]:
            _list_word[_index_changed_character - 1] = _list_char_dest[i]
            break
    elif _count_vowel == 3:
      _index_changed_character = _index_first_vowel + 1
      if _key == '7':
        for i in range(len(_list_char_sour)):
          if _list_word[_index_changed_character - 1] == _list_char_sour[i]:
            _list_word[_index_changed_character - 1] = _list_char_dest[i]
            break
    elif _count_vowel == 2:
      if _index_first_vowel + _count_vowel < len(_list_word):
        _index_changed_character = _index_first_vowel + 1
        if _key == '7' and _list_word[_index_first_vowel] != _list_word[_index_first_vowel + 1]:
          for i in range(len(_list_char_sour)):
            if _list_word[_index_changed_character - 1] == _list_char_sour[i]:
              _list_word[_index_changed_character - 1] = _list_char_dest[i]
              break
      else:
        if _key == '7' and _list_word[_index_first_vowel + 1] == 'o':
          _index_changed_character = _index_first_vowel + 1
        else:
          _index_changed_character = _index_first_vowel
    elif _count_vowel == 1:
      _index_changed_character = _index_first_vowel
    elif _key == '9':
      _index_changed_character = 0
    elif _count_vowel == 0:
      return word

    for i in range(len(_list_char_sour)):
      if _list_word[_index_changed_character] == _list_char_sour[i]:
        _list_word[_index_changed_character] = _list_char_dest[i]
        _has_changed = True
        break

    if _LAST_KEY == _key:
      if _pre_key != key:
        _list_word.append(_LAST_KEY)
    if _has_changed :
      _word = "".join(_list_word)
    return _word

class ControlimeCommand(sublime_plugin.TextCommand):
  _state_IME = True
  def run(self, edit):
    global _STATUS
    if self._state_IME == False:
      _STATUS = False
      self._state_IME = True
      sublime.status_message("VN IME Stoped")
      self.view.set_status('VN IME'," VN IME : OFF")
    elif self._state_IME :
      _STATUS = True
      self._state_IME = False
      sublime.status_message("VN IME Started")
      self.view.set_status('VN IME'," VN IME : ON")

class RunchangeCommand(sublime_plugin.TextCommand):
  def run(self, edit, _a, _b, _final):
    _char_region = sublime.Region(_a, _b)
    self.view.replace(edit,self.view.word(_char_region),_final)