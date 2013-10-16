# Include the Dropbox SDK
import dropbox
import json

# Get your app key and secret from the Dropbox developer website
app_key = 'tsyd07dln498sxc'
app_secret = '5r5hayqqbzf7yrw'

def get_access_token_and_user_id():
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    authorize_url = flow.start()
    print authorize_url
    code = raw_input("Enter the authorization code here: ").strip()
    access_token, user_id = flow.finish(code)
    print access_token, user_id
    return access_token, user_id;

def get_sample_access_token_and_user_id():
    return "7w2ssEkeZ6kAAAAAAAAAAR6cM3KPXOxk6ADVaR2gxD0f7zi7-oYHko2GJd5Brm9A" ,"51927223"

access_token, user_id = get_sample_access_token_and_user_id();
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

#f = open('working-draft.txt')
#response = client.put_file('/magnum-opus.txt', f)
#print "uploaded:", response

folder_metadata = client.metadata('/')
print
print json.dumps(folder_metadata, sort_keys=True, indent=4)



