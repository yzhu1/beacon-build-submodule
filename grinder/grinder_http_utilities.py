from com.xhaus.jyson import JysonCodec as json
import re

def getCsrfToken(self, result):
    sresultString = result.text
    csrfRegex = re.compile('name="ctoken" value="(\w+)"')
    regexMatch = csrfRegex.search(resultString)
    token = regexMatch.group(1)
    return token

def savePassage(self, testNumber, baseUrl, csrfToken, jsonArgs):
    headers = [NVPair('Accept', 'text/javascript, text/html, application/xml, text/xml, */*'),
               NVPair('Referer', '%s/oib/passage/create?fromManage=false' % baseUrl),
               NVPair('Cache-Control', 'no-cache'),
               NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')]
    request = HTTPRequest(url=baseUrl, headers=headers)
    request = Test(testNumber, 'POST savePassage').wrap(request)

    contentJSON = json.dumps(jsonArgs)
    formData = (NVPair('ctoken', csrfToken),
                NVPair('contentJSON', contentJSON),
                NVPair('subject', 'ELA'),
                NVPair('poolId', '35'))
    result = request.POST('/oib/savePassage', formData)
    return result

def savePassageTest(self, testNumber, baseUrl,pageResult, 
                    passageType='2', body='<p>Load test passage content</p>',
                    title='Load test passage5', subjectCode='ELA',
                    estTimeSecs='180',alignGrade={'from': '6', 'to': '8'}
                    ):    
    csrfToken = getCsrfToken(pageResult)
    jsonArgs = {'passageType': passageType,
                'body': body,
                'title': title,
                'subjectCode': subjectCode,
                'estTimeSecs': estTimeSecs,
                'alignGrade': alignGrade}
    result = savePassage(testNumber, url0, csrfToken, jsonArgs)
    passageVcid = json.loads(savePassageResult.text)['vcid']
    return passageVcid