
import conf
from dingtalk import AppKeyClient

config = getattr(conf, 'DINGTALK', {})
client = AppKeyClient(config['corp_id'], config['app_key'], config['app_secret'])