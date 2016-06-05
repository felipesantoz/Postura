import httplib, urllib, base64


class AzureRequest:

    def __init__(self):
        self.headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': 'a510a72d03224ec19e7307ab5ece8eff',
        }

        self.params = urllib.urlencode({
            # Request parameters
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'true',
            'returnFaceAttributes': '',
        })

    def request(self, body):
        try:
            conn = httplib.HTTPSConnection('api.projectoxford.ai')
            conn.request("POST", "/face/v1.0/detect?%s" % self.params, body, self.headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return data

####################################
