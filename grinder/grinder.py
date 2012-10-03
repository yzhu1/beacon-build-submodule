# The Grinder 3.4
# HTTP script recorded by TCPProxy at Dec 28, 2010 12:57:31 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Language', 'en-us,en;q=0.5'),
    NVPair('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),
    NVPair('Accept-Encoding', 'gzip,deflate'),
    NVPair('User-Agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.14) Gecko/2009091106 CentOS/3.0.14-1.el5.centos Firefox/3.0.14'), ]

headers0= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers1= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/home'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers2= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/home'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers3= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/common/css/widgets/GlobalNavBar.css'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers4= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/common/css/skin.css'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers5= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/common/css/basic.css'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers6= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/home'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers7= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/css/dashboard.css'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers8= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/common/css/widgets/mClassNavBar.css'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers9= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/home'), ]

headers10= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/css/manage/manage_assessment.css'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers11= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/css/jquery-ui-1.7.2.custom.css'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers12= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/home'),
    NVPair('Cache-Control', 'no-cache'), ]

headers13= \
  [ NVPair('Accept', 'text/javascript, application/javascript, */*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/home'), ]

headers14= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/css/view_entity.css'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers15= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/css/widgets/shopping_cart.css'),
    NVPair('Cache-Control', 'max-age=0'), ]

headers16= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/home'), ]

headers17= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/assessment/clone?id=342'),
    NVPair('Cache-Control', 'no-cache'), ]

headers18= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/assessment/clone?id=342'), ]

headers19= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers20= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/assessment/clone?id=342'),
    NVPair('Cache-Control', 'no-cache'), ]

headers21= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/assessment/clone?id=342'), ]

headers22= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/outcomes/report/view'), ]

headers23= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/outcomes/report/view'), ]

headers24= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/outcomes/report/view'), ]

headers25= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/outcomes/static/css/widgets/featheredBox.css'), ]

headers26= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/outcomes/static/css/widgets/buttonBar.css'), ]

headers27= \
  [ NVPair('Accept', 'text/javascript, text/html, application/xml, text/xml, */*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/outcomes/report/view'), ]

headers28= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/outcomes/static/css/learning_map.css'), ]

headers29= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/outcomes/static/css/learning_map_legend.css'), ]

headers30= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/outcomes/static/js/hexmap/assets/honeycomb.css'), ]

headers31= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/outcomes/report/view'), ]

headers32= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/item/create?fromManage=false'), ]

headers33= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/item/create?fromManage=false'), ]

headers34= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/common/css/basic.css'), ]

headers35= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/css/create/create.css'), ]

headers36= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/item/create?fromManage=false'), ]

headers37= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/css/standards_create.css'), ]

headers38= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/item/create?fromManage=false'), ]

headers39= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/css/jquery-ui-1.7.2.custom.css'), ]

headers40= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui.css'), ]

headers41= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui_threetwelve.css'), ]

headers42= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/static/css/manage/manage.css'), ]

headers43= \
  [ NVPair('Accept', 'text/javascript, application/javascript, */*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/item/create?fromManage=false'), ]

headers44= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/item/create?fromManage=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers45= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'https://mclasshome-loadtest.wgenhq.net/oib/item/create?fromManage=false'),
    NVPair('Cache-Control', 'no-cache'), ]

url0 = 'https://mclasshome-loadtest.wgenhq.net:443'
url1 = 'http://safebrowsing.clients.google.com:80'
url2 = 'http://safebrowsing-cache.google.com:80'

# Create an HTTPRequest for each request, then replace the
# reference to the HTTPRequest with an instrumented version.
# You can access the unadorned instance using request101.__target__.
# started proxy
request101 = HTTPRequest(url=url0, headers=headers0)
request101 = Test(101, 'GET login').wrap(request101)

request102 = HTTPRequest(url=url0, headers=headers0)
request102 = Test(102, 'GET home').wrap(request102)

request103 = HTTPRequest(url=url0, headers=headers1)
request103 = Test(103, 'GET GlobalNavBar.css').wrap(request103)

request104 = HTTPRequest(url=url0, headers=headers1)
request104 = Test(104, 'GET mClassNavBar.css').wrap(request104)

request105 = HTTPRequest(url=url0, headers=headers1)
request105 = Test(105, 'GET jquery-ui-1.7.2.custom.css').wrap(request105)

request106 = HTTPRequest(url=url0, headers=headers1)
request106 = Test(106, 'GET basic.css').wrap(request106)

request107 = HTTPRequest(url=url0, headers=headers1)
request107 = Test(107, 'GET skin.css').wrap(request107)

request108 = HTTPRequest(url=url0, headers=headers1)
request108 = Test(108, 'GET styled_text.css').wrap(request108)

request109 = HTTPRequest(url=url0, headers=headers1)
request109 = Test(109, 'GET standards.css').wrap(request109)

request110 = HTTPRequest(url=url0, headers=headers1)
request110 = Test(110, 'GET help.css').wrap(request110)

request111 = HTTPRequest(url=url0, headers=headers2)
request111 = Test(111, 'GET logo_mclass_navbar.gif').wrap(request111)

request112 = HTTPRequest(url=url0, headers=headers2)
request112 = Test(112, 'GET px.gif').wrap(request112)

request113 = HTTPRequest(url=url0, headers=headers2)
request113 = Test(113, 'GET icon_question_contextual.gif').wrap(request113)

request114 = HTTPRequest(url=url0, headers=headers2)
request114 = Test(114, 'GET navbar_logo.gif').wrap(request114)

request115 = HTTPRequest(url=url0, headers=headers3)
request115 = Test(115, 'GET navigation_buttons_sprite.png').wrap(request115)

request116 = HTTPRequest(url=url0, headers=headers3)
request116 = Test(116, 'GET navigation_buttons_icons_sprite.png').wrap(request116)

request117 = HTTPRequest(url=url0, headers=headers4)
request117 = Test(117, 'GET assess_back.png').wrap(request117)

request118 = HTTPRequest(url=url0, headers=headers1)
request118 = Test(118, 'GET manage.css').wrap(request118)

request119 = HTTPRequest(url=url0, headers=headers1)
request119 = Test(119, 'GET manage_item.css').wrap(request119)

request120 = HTTPRequest(url=url0, headers=headers1)
request120 = Test(120, 'GET manage_passage.css').wrap(request120)

request121 = HTTPRequest(url=url0, headers=headers1)
request121 = Test(121, 'GET dashboard.css').wrap(request121)

request122 = HTTPRequest(url=url0, headers=headers1)
request122 = Test(122, 'GET manage_rubric.css').wrap(request122)

request123 = HTTPRequest(url=url0, headers=headers1)
request123 = Test(123, 'GET manage_assessment.css').wrap(request123)

request124 = HTTPRequest(url=url0, headers=headers5)
request124 = Test(124, 'GET table_contents_bottom_tile.gif').wrap(request124)

request125 = HTTPRequest(url=url0, headers=headers1)
request125 = Test(125, 'GET jqueryMultiSelect.css').wrap(request125)

request126 = HTTPRequest(url=url0, headers=headers1)
request126 = Test(126, 'GET view_entity.css').wrap(request126)

request127 = HTTPRequest(url=url0, headers=headers5)
request127 = Test(127, 'GET table_contents_right_tile.gif').wrap(request127)

request128 = HTTPRequest(url=url0, headers=headers4)
request128 = Test(128, 'GET body_content_area_corner_sprite.png').wrap(request128)

request129 = HTTPRequest(url=url0, headers=headers5)
request129 = Test(129, 'GET table_contents_corners_sprite.gif').wrap(request129)

request130 = HTTPRequest(url=url0, headers=headers5)
request130 = Test(130, 'GET ajax-loader-lrg.gif').wrap(request130)

request131 = HTTPRequest(url=url0, headers=headers6)
request131 = Test(131, 'GET closure.base.js').wrap(request131)

request132 = HTTPRequest(url=url0, headers=headers7)
request132 = Test(132, 'GET video_box_gradient.png').wrap(request132)

request133 = HTTPRequest(url=url0, headers=headers6)
request133 = Test(133, 'GET jquery-1.3.2.js').wrap(request133)

request134 = HTTPRequest(url=url0, headers=headers6)
request134 = Test(134, 'GET ui.core.js').wrap(request134)

request135 = HTTPRequest(url=url0, headers=headers6)
request135 = Test(135, 'GET ui.draggable.js').wrap(request135)

request136 = HTTPRequest(url=url0, headers=headers6)
request136 = Test(136, 'GET ui.sortable.js').wrap(request136)

request137 = HTTPRequest(url=url0, headers=headers8)
request137 = Test(137, 'GET bg_header_blue_dot.gif').wrap(request137)

request138 = HTTPRequest(url=url0, headers=headers6)
request138 = Test(138, 'GET ui.resizable.js').wrap(request138)

request139 = HTTPRequest(url=url0, headers=headers6)
request139 = Test(139, 'GET ui.slider.js').wrap(request139)

request140 = HTTPRequest(url=url0, headers=headers6)
request140 = Test(140, 'GET ui.dialog.js').wrap(request140)

request141 = HTTPRequest(url=url0, headers=headers6)
request141 = Test(141, 'GET ui.tabs.js').wrap(request141)

request142 = HTTPRequest(url=url0, headers=headers6)
request142 = Test(142, 'GET jquery_setup.js').wrap(request142)

request143 = HTTPRequest(url=url0, headers=headers6)
request143 = Test(143, 'GET prototype.js').wrap(request143)

request144 = HTTPRequest(url=url0, headers=headers6)
request144 = Test(144, 'GET jquery.form.js').wrap(request144)

request145 = HTTPRequest(url=url0, headers=headers6)
request145 = Test(145, 'GET jquery.tooltip.js').wrap(request145)

request146 = HTTPRequest(url=url0, headers=headers6)
request146 = Test(146, 'GET autoresize.jquery.min.js').wrap(request146)

request147 = HTTPRequest(url=url0, headers=headers6)
request147 = Test(147, 'GET jsonStringify.js').wrap(request147)

request148 = HTTPRequest(url=url0, headers=headers5)
request148 = Test(148, 'GET top_bar_divider.gif').wrap(request148)

request149 = HTTPRequest(url=url0, headers=headers6)
request149 = Test(149, 'GET LaTeXMathML.js').wrap(request149)

request150 = HTTPRequest(url=url0, headers=headers6)
request150 = Test(150, 'GET math-utilities.js').wrap(request150)

request151 = HTTPRequest(url=url0, headers=headers6)
request151 = Test(151, 'GET standardsUi.js').wrap(request151)

request152 = HTTPRequest(url=url0, headers=headers6)
request152 = Test(152, 'GET standards.js').wrap(request152)

request153 = HTTPRequest(url=url0, headers=headers6)
request153 = Test(153, 'GET BackspaceSuppress.js').wrap(request153)

request154 = HTTPRequest(url=url0, headers=headers6)
request154 = Test(154, 'GET TimeoutDetect.js').wrap(request154)

request155 = HTTPRequest(url=url0, headers=headers6)
request155 = Test(155, 'GET global_ready.js').wrap(request155)

request156 = HTTPRequest(url=url0, headers=headers6)
request156 = Test(156, 'GET wgen.oib.utilities.js').wrap(request156)

request157 = HTTPRequest(url=url0, headers=headers6)
request157 = Test(157, 'GET RoboHelp_CSH.js').wrap(request157)

request158 = HTTPRequest(url=url0, headers=headers6)
request158 = Test(158, 'GET help.js').wrap(request158)

request159 = HTTPRequest(url=url0, headers=headers6)
request159 = Test(159, 'GET jquery_functions.js').wrap(request159)

request160 = HTTPRequest(url=url0, headers=headers6)
request160 = Test(160, 'GET cookieHandler.js').wrap(request160)

request161 = HTTPRequest(url=url0, headers=headers6)
request161 = Test(161, 'GET googleAnalytics.js').wrap(request161)

request162 = HTTPRequest(url=url0, headers=headers6)
request162 = Test(162, 'GET ViewItemBankEntity.js').wrap(request162)

request163 = HTTPRequest(url=url0, headers=headers6)
request163 = Test(163, 'GET sharing.js').wrap(request163)

request164 = HTTPRequest(url=url0, headers=headers6)
request164 = Test(164, 'GET createStandardsUi.js').wrap(request164)

request165 = HTTPRequest(url=url0, headers=headers6)
request165 = Test(165, 'GET viewStandardsUi.js').wrap(request165)

request166 = HTTPRequest(url=url0, headers=headers6)
request166 = Test(166, 'GET SharingDropdown.js').wrap(request166)

request167 = HTTPRequest(url=url0, headers=headers6)
request167 = Test(167, 'GET jqueryMultiSelect.js').wrap(request167)

request168 = HTTPRequest(url=url0, headers=headers6)
request168 = Test(168, 'GET tooltip.js').wrap(request168)

request169 = HTTPRequest(url=url0, headers=headers6)
request169 = Test(169, 'GET EntityPopupSourceUI.js').wrap(request169)

request170 = HTTPRequest(url=url0, headers=headers6)
request170 = Test(170, 'GET ManageBrowser.js').wrap(request170)

request171 = HTTPRequest(url=url0, headers=headers6)
request171 = Test(171, 'GET ManageBrowserRenderer.js').wrap(request171)

request172 = HTTPRequest(url=url0, headers=headers6)
request172 = Test(172, 'GET ManageItemBrowserRenderer.js').wrap(request172)

request173 = HTTPRequest(url=url0, headers=headers6)
request173 = Test(173, 'GET ManagePassageBrowserRenderer.js').wrap(request173)

request174 = HTTPRequest(url=url0, headers=headers6)
request174 = Test(174, 'GET ManageRubricBrowserRenderer.js').wrap(request174)

request175 = HTTPRequest(url=url0, headers=headers6)
request175 = Test(175, 'GET ManageAssessmentBrowserRenderer.js').wrap(request175)

request176 = HTTPRequest(url=url0, headers=headers6)
request176 = Test(176, 'GET RecentEntityWidget.js').wrap(request176)

request177 = HTTPRequest(url=url0, headers=headers6)
request177 = Test(177, 'GET DashboardPage.js').wrap(request177)

request178 = HTTPRequest(url=url0, headers=headers6)
request178 = Test(178, 'GET dashboard_ready.js').wrap(request178)

request179 = HTTPRequest(url=url0, headers=headers6)
request179 = Test(179, 'GET QuestionType.js').wrap(request179)

request180 = HTTPRequest(url=url0, headers=headers6)
request180 = Test(180, 'GET OpenResponseQuestionType.js').wrap(request180)

request181 = HTTPRequest(url=url0, headers=headers6)
request181 = Test(181, 'GET GlobalNavBar.js').wrap(request181)

request201 = HTTPRequest(url=url0, headers=headers9)
request201 = Test(201, 'GET recent').wrap(request201)

request202 = HTTPRequest(url=url0, headers=headers5)
request202 = Test(202, 'GET blue_button_flat.gif').wrap(request202)

request301 = HTTPRequest(url=url0, headers=headers0)
request301 = Test(301, 'GET ellipsis.xml').wrap(request301)

request302 = HTTPRequest(url=url0, headers=headers10)
request302 = Test(302, 'GET locate_rounded_corner_objects.png').wrap(request302)

request303 = HTTPRequest(url=url0, headers=headers10)
request303 = Test(303, 'GET sprites.png').wrap(request303)

request304 = HTTPRequest(url=url0, headers=headers10)
request304 = Test(304, 'GET assessment_item_count_box.png').wrap(request304)

# opened a link
request305 = HTTPRequest(url=url0, headers=headers11)
request305 = Test(305, 'GET border.png').wrap(request305)

request306 = HTTPRequest(url=url0, headers=headers11)
request306 = Test(306, 'GET close_X.png').wrap(request306)

request401 = HTTPRequest(url=url0, headers=headers12)
request401 = Test(401, 'POST base').wrap(request401)

request402 = HTTPRequest(url=url0, headers=headers2)
request402 = Test(402, 'GET icon_edit.png').wrap(request402)

request403 = HTTPRequest(url=url0, headers=headers2)
request403 = Test(403, 'GET icon_delete.png').wrap(request403)

request404 = HTTPRequest(url=url0, headers=headers13)
request404 = Test(404, 'GET Ajax.js').wrap(request404)

request405 = HTTPRequest(url=url0, headers=headers13)
request405 = Test(405, 'GET Button.js').wrap(request405)

request406 = HTTPRequest(url=url0, headers=headers2)
request406 = Test(406, 'GET icon_cloneAndEdit.png').wrap(request406)

request407 = HTTPRequest(url=url0, headers=headers13)
request407 = Test(407, 'GET jqueryMultiSelect.js').wrap(request407)

request408 = HTTPRequest(url=url0, headers=headers13)
request408 = Test(408, 'GET PopulationHierarchyBrowser.js').wrap(request408)

request409 = HTTPRequest(url=url0, headers=headers2)
request409 = Test(409, 'GET icon_print.png').wrap(request409)

request410 = HTTPRequest(url=url0, headers=headers13)
request410 = Test(410, 'GET PopulationHierarchyBrowserData.js').wrap(request410)

request411 = HTTPRequest(url=url0, headers=headers2)
request411 = Test(411, 'GET tooltip_win_arrow_top.png').wrap(request411)

request412 = HTTPRequest(url=url0, headers=headers13)
request412 = Test(412, 'GET PopulationHierarchyBrowserUI.js').wrap(request412)

request413 = HTTPRequest(url=url0, headers=headers13)
request413 = Test(413, 'GET AssignmentCreator.js').wrap(request413)

request414 = HTTPRequest(url=url0, headers=headers13)
request414 = Test(414, 'GET AssignmentViewer.js').wrap(request414)

request415 = HTTPRequest(url=url0, headers=headers13)
request415 = Test(415, 'GET MyAssignmentsPage.js').wrap(request415)

request501 = HTTPRequest(url=url0, headers=headers9)
request501 = Test(501, 'GET list').wrap(request501)

request601 = HTTPRequest(url=url0, headers=headers9)
request601 = Test(601, 'GET create').wrap(request601)

request602 = HTTPRequest(url=url0, headers=headers13)
request602 = Test(602, 'GET sharing.js').wrap(request602)

request603 = HTTPRequest(url=url0, headers=headers13)
request603 = Test(603, 'GET SharingDropdown.js').wrap(request603)

request604 = HTTPRequest(url=url0, headers=headers14)
request604 = Test(604, 'GET overview_vert.gif').wrap(request604)

request605 = HTTPRequest(url=url0, headers=headers14)
request605 = Test(605, 'GET overview_tr.gif').wrap(request605)

request606 = HTTPRequest(url=url0, headers=headers14)
request606 = Test(606, 'GET overview_tl.gif').wrap(request606)

request607 = HTTPRequest(url=url0, headers=headers14)
request607 = Test(607, 'GET overview_horiz.gif').wrap(request607)

request608 = HTTPRequest(url=url0, headers=headers15)
request608 = Test(608, 'GET rounded_corner_yellow_top.png').wrap(request608)

request609 = HTTPRequest(url=url0, headers=headers2)
request609 = Test(609, 'GET icon_assignment.gif').wrap(request609)

request610 = HTTPRequest(url=url0, headers=headers15)
request610 = Test(610, 'GET rounded_corner_yellow_horiz_bg.png').wrap(request610)

request611 = HTTPRequest(url=url0, headers=headers15)
request611 = Test(611, 'GET rounded_corner_yellow_vert_bg.png').wrap(request611)

request701 = HTTPRequest(url=url0, headers=headers16)
request701 = Test(701, 'GET clone').wrap(request701)

request801 = HTTPRequest(url=url0, headers=headers17)
request801 = Test(801, 'POST sharingAgreement').wrap(request801)

request901 = HTTPRequest(url=url0, headers=headers18)
request901 = Test(901, 'GET keepalive').wrap(request901)

request1001 = HTTPRequest(url=url1, headers=headers19)
request1001 = Test(1001, 'POST downloads').wrap(request1001)

request1101 = HTTPRequest(url=url2, headers=headers19)
request1101 = Test(1101, 'GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAEY79QCIPjUAioGcKoAAP8BMgVvqgAAAQ').wrap(request1101)

request1201 = HTTPRequest(url=url2, headers=headers19)
request1201 = Test(1201, 'GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYodgBIMDZATIZIWwAAP____-__7f7v_____3____f__7_AA').wrap(request1201)

request1301 = HTTPRequest(url=url2, headers=headers19)
request1301 = Test(1301, 'GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYwegBIIDrATItQXQAAP_v_______v_9______7______vv___9____9_v7_7_9__-_9____cA').wrap(request1301)

request1401 = HTTPRequest(url=url2, headers=headers19)
request1401 = Test(1401, 'GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYgesBIMDtATItgXUAAP3__-_____9___v______-______________3___________v6__78A').wrap(request1401)

request1501 = HTTPRequest(url=url2, headers=headers19)
request1501 = Test(1501, 'GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYwe0BIIDwATItwXYAAP____v___d_3____vf7_f_____7__________________________8A').wrap(request1501)

request1601 = HTTPRequest(url=url2, headers=headers19)
request1601 = Test(1601, 'GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYgfABIICEAiqoAuR4AAD___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________8fMiEBeAAA_7_ff_9______________________________wc').wrap(request1601)

request1701 = HTTPRequest(url=url2, headers=headers19)
request1701 = Test(1701, 'GET ChFnb29nLXBoaXNoLXNoYXZhchABGLGCBCCAgwQyDzEBAQD_____-_______AA').wrap(request1701)

request1801 = HTTPRequest(url=url2, headers=headers19)
request1801 = Test(1801, 'GET ChFnb29nLXBoaXNoLXNoYXZhchABGIGDBCCAiAQyVYEBAQD___9________________________________3_____________________________________________________________________wA').wrap(request1801)

request1901 = HTTPRequest(url=url0, headers=headers20)
request1901 = Test(1901, 'POST save').wrap(request1901)

request2001 = HTTPRequest(url=url0, headers=headers21)
request2001 = Test(2001, 'GET view').wrap(request2001)

request2002 = HTTPRequest(url=url0, headers=headers22)
request2002 = Test(2002, 'GET basic.css').wrap(request2002)

request2003 = HTTPRequest(url=url0, headers=headers22)
request2003 = Test(2003, 'GET skin.css').wrap(request2003)

request2004 = HTTPRequest(url=url0, headers=headers22)
request2004 = Test(2004, 'GET GlobalNavBar.css').wrap(request2004)

request2005 = HTTPRequest(url=url0, headers=headers22)
request2005 = Test(2005, 'GET jquery-ui-1.7.2.custom.css').wrap(request2005)

request2006 = HTTPRequest(url=url0, headers=headers22)
request2006 = Test(2006, 'GET mClassNavBar.css').wrap(request2006)

request2007 = HTTPRequest(url=url0, headers=headers23)
request2007 = Test(2007, 'GET logo_mclass_navbar.gif').wrap(request2007)

request2008 = HTTPRequest(url=url0, headers=headers23)
request2008 = Test(2008, 'GET icon_question_contextual.gif').wrap(request2008)

request2009 = HTTPRequest(url=url0, headers=headers23)
request2009 = Test(2009, 'GET px.gif').wrap(request2009)

request2010 = HTTPRequest(url=url0, headers=headers22)
request2010 = Test(2010, 'GET reports.css').wrap(request2010)

request2011 = HTTPRequest(url=url0, headers=headers22)
request2011 = Test(2011, 'GET matrix.css').wrap(request2011)

request2012 = HTTPRequest(url=url0, headers=headers22)
request2012 = Test(2012, 'GET learning_map_legend.css').wrap(request2012)

request2013 = HTTPRequest(url=url0, headers=headers22)
request2013 = Test(2013, 'GET learning_map.css').wrap(request2013)

request2014 = HTTPRequest(url=url0, headers=headers22)
request2014 = Test(2014, 'GET ellipsis.css').wrap(request2014)

request2015 = HTTPRequest(url=url0, headers=headers22)
request2015 = Test(2015, 'GET featheredBox.css').wrap(request2015)

request2016 = HTTPRequest(url=url0, headers=headers23)
request2016 = Test(2016, 'GET navbar_logo.gif').wrap(request2016)

request2017 = HTTPRequest(url=url0, headers=headers22)
request2017 = Test(2017, 'GET buttonBar.css').wrap(request2017)

request2018 = HTTPRequest(url=url0, headers=headers22)
request2018 = Test(2018, 'GET honeycomb.css').wrap(request2018)

request2019 = HTTPRequest(url=url0, headers=headers22)
request2019 = Test(2019, 'GET item_analysis.css').wrap(request2019)

request2020 = HTTPRequest(url=url0, headers=headers22)
request2020 = Test(2020, 'GET standard_analysis.css').wrap(request2020)

request2021 = HTTPRequest(url=url0, headers=headers24)
request2021 = Test(2021, 'GET closure.base.js').wrap(request2021)

request2022 = HTTPRequest(url=url0, headers=headers25)
request2022 = Test(2022, 'GET feathered_box_vert.png').wrap(request2022)

request2023 = HTTPRequest(url=url0, headers=headers25)
request2023 = Test(2023, 'GET feathered_box_horiz.png').wrap(request2023)

request2024 = HTTPRequest(url=url0, headers=headers25)
request2024 = Test(2024, 'GET feathered_box.png').wrap(request2024)

request2025 = HTTPRequest(url=url0, headers=headers26)
request2025 = Test(2025, 'GET button_gel.png').wrap(request2025)

request2026 = HTTPRequest(url=url0, headers=headers22)
request2026 = Test(2026, 'GET dropdownControl.css').wrap(request2026)

request2027 = HTTPRequest(url=url0, headers=headers22)
request2027 = Test(2027, 'GET report_colors.css').wrap(request2027)

request2028 = HTTPRequest(url=url0, headers=headers24)
request2028 = Test(2028, 'GET jquery-1.3.2.js').wrap(request2028)

request2029 = HTTPRequest(url=url0, headers=headers24)
request2029 = Test(2029, 'GET ui.core.js').wrap(request2029)

request2030 = HTTPRequest(url=url0, headers=headers24)
request2030 = Test(2030, 'GET ui.draggable.js').wrap(request2030)

request2031 = HTTPRequest(url=url0, headers=headers24)
request2031 = Test(2031, 'GET ui.sortable.js').wrap(request2031)

request2032 = HTTPRequest(url=url0, headers=headers24)
request2032 = Test(2032, 'GET ui.resizable.js').wrap(request2032)

request2033 = HTTPRequest(url=url0, headers=headers24)
request2033 = Test(2033, 'GET ui.slider.js').wrap(request2033)

request2034 = HTTPRequest(url=url0, headers=headers24)
request2034 = Test(2034, 'GET ui.dialog.js').wrap(request2034)

request2035 = HTTPRequest(url=url0, headers=headers24)
request2035 = Test(2035, 'GET ui.tabs.js').wrap(request2035)

request2036 = HTTPRequest(url=url0, headers=headers24)
request2036 = Test(2036, 'GET jquery_functions.js').wrap(request2036)

request2037 = HTTPRequest(url=url0, headers=headers24)
request2037 = Test(2037, 'GET jquery_setup.js').wrap(request2037)

request2038 = HTTPRequest(url=url0, headers=headers24)
request2038 = Test(2038, 'GET prototype.js').wrap(request2038)

request2039 = HTTPRequest(url=url0, headers=headers24)
request2039 = Test(2039, 'GET jquery.form.js').wrap(request2039)

request2040 = HTTPRequest(url=url0, headers=headers24)
request2040 = Test(2040, 'GET autoresize.jquery.min.js').wrap(request2040)

request2041 = HTTPRequest(url=url0, headers=headers24)
request2041 = Test(2041, 'GET jquery.tooltip.js').wrap(request2041)

request2042 = HTTPRequest(url=url0, headers=headers24)
request2042 = Test(2042, 'GET BackspaceSuppress.js').wrap(request2042)

request2043 = HTTPRequest(url=url0, headers=headers24)
request2043 = Test(2043, 'GET TimeoutDetect.js').wrap(request2043)

request2044 = HTTPRequest(url=url0, headers=headers24)
request2044 = Test(2044, 'GET global_ready.js').wrap(request2044)

request2045 = HTTPRequest(url=url0, headers=headers24)
request2045 = Test(2045, 'GET wgen.oib.utilities.js').wrap(request2045)

request2046 = HTTPRequest(url=url0, headers=headers24)
request2046 = Test(2046, 'GET RoboHelp_CSH.js').wrap(request2046)

request2047 = HTTPRequest(url=url0, headers=headers24)
request2047 = Test(2047, 'GET help.js').wrap(request2047)

request2048 = HTTPRequest(url=url0, headers=headers24)
request2048 = Test(2048, 'GET cookieHandler.js').wrap(request2048)

request2049 = HTTPRequest(url=url0, headers=headers24)
request2049 = Test(2049, 'GET googleAnalytics.js').wrap(request2049)

request2050 = HTTPRequest(url=url0, headers=headers24)
request2050 = Test(2050, 'GET DropdownControl.js').wrap(request2050)

request2051 = HTTPRequest(url=url0, headers=headers24)
request2051 = Test(2051, 'GET ClasseAndAssessmentDropdownPicker.js').wrap(request2051)

request2052 = HTTPRequest(url=url0, headers=headers24)
request2052 = Test(2052, 'GET ClasseAndAssessmentDropdownPickerData.js').wrap(request2052)

request2053 = HTTPRequest(url=url0, headers=headers24)
request2053 = Test(2053, 'GET ButtonBar.js').wrap(request2053)

request2054 = HTTPRequest(url=url0, headers=headers24)
request2054 = Test(2054, 'GET HoneycombWidgetUI.js').wrap(request2054)

request2055 = HTTPRequest(url=url0, headers=headers24)
request2055 = Test(2055, 'GET HoneycombEvent.js').wrap(request2055)

request2056 = HTTPRequest(url=url0, headers=headers24)
request2056 = Test(2056, 'GET TileManager.js').wrap(request2056)

request2057 = HTTPRequest(url=url0, headers=headers24)
request2057 = Test(2057, 'GET TileManagerUtil.js').wrap(request2057)

request2058 = HTTPRequest(url=url0, headers=headers24)
request2058 = Test(2058, 'GET HoneycombWidget.js').wrap(request2058)

request2059 = HTTPRequest(url=url0, headers=headers24)
request2059 = Test(2059, 'GET LearningMapUtil.js').wrap(request2059)

request2060 = HTTPRequest(url=url0, headers=headers24)
request2060 = Test(2060, 'GET Config.js').wrap(request2060)

request2061 = HTTPRequest(url=url0, headers=headers24)
request2061 = Test(2061, 'GET Ajax.js').wrap(request2061)

request2062 = HTTPRequest(url=url0, headers=headers24)
request2062 = Test(2062, 'GET ItemAnalysisOverlay.js').wrap(request2062)

request2063 = HTTPRequest(url=url0, headers=headers24)
request2063 = Test(2063, 'GET ItemAnalysisData.js').wrap(request2063)

request2064 = HTTPRequest(url=url0, headers=headers24)
request2064 = Test(2064, 'GET StandardAnalysisOverlay.js').wrap(request2064)

request2065 = HTTPRequest(url=url0, headers=headers24)
request2065 = Test(2065, 'GET StandardAnalysisData.js').wrap(request2065)

request2066 = HTTPRequest(url=url0, headers=headers24)
request2066 = Test(2066, 'GET MatrixUI.js').wrap(request2066)

request2067 = HTTPRequest(url=url0, headers=headers24)
request2067 = Test(2067, 'GET MatrixData.js').wrap(request2067)

request2068 = HTTPRequest(url=url0, headers=headers24)
request2068 = Test(2068, 'GET LearningMapUI.js').wrap(request2068)

request2069 = HTTPRequest(url=url0, headers=headers24)
request2069 = Test(2069, 'GET LearningMapData.js').wrap(request2069)

request2070 = HTTPRequest(url=url0, headers=headers24)
request2070 = Test(2070, 'GET ReportsUI.js').wrap(request2070)

request2071 = HTTPRequest(url=url0, headers=headers24)
request2071 = Test(2071, 'GET ReportsPage.js').wrap(request2071)

request2072 = HTTPRequest(url=url0, headers=headers24)
request2072 = Test(2072, 'GET reports_ready.js').wrap(request2072)

request2073 = HTTPRequest(url=url0, headers=headers24)
request2073 = Test(2073, 'GET InstHierarchyDropdownPicker.js').wrap(request2073)

request2074 = HTTPRequest(url=url0, headers=headers24)
request2074 = Test(2074, 'GET GlobalNavBar.js').wrap(request2074)

request2101 = HTTPRequest(url=url0, headers=headers27)
request2101 = Test(2101, 'GET staff').wrap(request2101)

request2201 = HTTPRequest(url=url0, headers=headers27)
request2201 = Test(2201, 'GET classes').wrap(request2201)

request2301 = HTTPRequest(url=url0, headers=headers27)
request2301 = Test(2301, 'GET assessments').wrap(request2301)

request2401 = HTTPRequest(url=url0, headers=headers27)
request2401 = Test(2401, 'GET studentList').wrap(request2401)

request2402 = HTTPRequest(url=url0, headers=headers28)
request2402 = Test(2402, 'GET ajax-loader-lrg.gif').wrap(request2402)

request2501 = HTTPRequest(url=url0, headers=headers27)
request2501 = Test(2501, 'GET classeMap').wrap(request2501)

request2502 = HTTPRequest(url=url0, headers=headers23)
request2502 = Test(2502, 'GET click_to_open.png').wrap(request2502)

request2503 = HTTPRequest(url=url0, headers=headers23)
request2503 = Test(2503, 'GET click_to_close.png').wrap(request2503)

request2504 = HTTPRequest(url=url0, headers=headers28)
request2504 = Test(2504, 'GET student_list_header.png').wrap(request2504)

request2505 = HTTPRequest(url=url0, headers=headers28)
request2505 = Test(2505, 'GET icon_student_not_faded.png').wrap(request2505)

request2506 = HTTPRequest(url=url0, headers=headers28)
request2506 = Test(2506, 'GET cells.png').wrap(request2506)

request2601 = HTTPRequest(url=url0, headers=headers19)
request2601 = Test(2601, 'GET ellipsis.xml').wrap(request2601)

request2602 = HTTPRequest(url=url0, headers=headers28)
request2602 = Test(2602, 'GET question_mark_cell.png').wrap(request2602)

request2603 = HTTPRequest(url=url0, headers=headers29)
request2603 = Test(2603, 'GET legend_tab.png').wrap(request2603)

request2604 = HTTPRequest(url=url0, headers=headers30)
request2604 = Test(2604, 'GET clear.gif').wrap(request2604)

request2605 = HTTPRequest(url=url0, headers=headers30)
request2605 = Test(2605, 'GET ui_tile_dark.png').wrap(request2605)

request2606 = HTTPRequest(url=url0, headers=headers30)
request2606 = Test(2606, 'GET ui_sprite.png').wrap(request2606)

request2701 = HTTPRequest(url=url0, headers=headers27)
request2701 = Test(2701, 'GET info').wrap(request2701)

request2702 = HTTPRequest(url=url0, headers=headers30)
request2702 = Test(2702, 'GET ui_grid_tile.png').wrap(request2702)

request2703 = HTTPRequest(url=url0, headers=headers30)
request2703 = Test(2703, 'GET ui_pan.png').wrap(request2703)

request2801 = HTTPRequest(url=url0, headers=headers23)
request2801 = Test(2801, 'GET tile').wrap(request2801)

request2901 = HTTPRequest(url=url0, headers=headers23)
request2901 = Test(2901, 'GET tile').wrap(request2901)

request3001 = HTTPRequest(url=url0, headers=headers23)
request3001 = Test(3001, 'GET tile').wrap(request3001)

request3101 = HTTPRequest(url=url2, headers=headers19)
request3101 = Test(3101, 'GET ChFnb29nLXBoaXNoLXNoYXZhchABGIGIBCCAnAQqwgIVBAEA______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________8PMgcBBAEA__8P').wrap(request3101)

request3201 = HTTPRequest(url=url2, headers=headers19)
request3201 = Test(3201, 'GET ChFnb29nLXBoaXNoLXNoYXZhchAAGIHjByCA6AcyVYHxAQD___________________v_9ff________f7__9_____89_ev__df_______3_uuf7_93v_8773__-isv_______2-1tfPjf3in3r38X9n-_wA').wrap(request3201)

request3301 = HTTPRequest(url=url2, headers=headers19)
request3301 = Test(3301, 'GET ChFnb29nLXBoaXNoLXNoYXZhchAAGIHoByDA6gcyLQH0AQD____f___vf_X__________f____________v___3___v_________AA').wrap(request3301)

request3401 = HTTPRequest(url=url2, headers=headers19)
request3401 = Test(3401, 'GET ChFnb29nLXBoaXNoLXNoYXZhchAAGMHqByCA7QcyLEL1AQD_______________________________________f___________9_').wrap(request3401)

request3501 = HTTPRequest(url=url2, headers=headers19)
request3501 = Test(3501, 'GET ChFnb29nLXBoaXNoLXNoYXZhchAAGIHtByDA7wcyLYH2AQD_____________________________________________________AA').wrap(request3501)

request3601 = HTTPRequest(url=url2, headers=headers19)
request3601 = Test(3601, 'GET ChFnb29nLXBoaXNoLXNoYXZhchAAGMHvByCA8gcqHEL4AQD______________________________38yFcH3AQD_____________________AQ').wrap(request3601)

# DONE WITH MAP
# GOING TO DASHBOARD
request3701 = HTTPRequest(url=url0, headers=headers31)
request3701 = Test(3701, 'GET home').wrap(request3701)

request3801 = HTTPRequest(url=url0, headers=headers9)
request3801 = Test(3801, 'GET recent').wrap(request3801)

request3901 = HTTPRequest(url=url0, headers=headers12)
request3901 = Test(3901, 'POST base').wrap(request3901)

request3902 = HTTPRequest(url=url0, headers=headers13)
request3902 = Test(3902, 'GET Ajax.js').wrap(request3902)

request3903 = HTTPRequest(url=url0, headers=headers13)
request3903 = Test(3903, 'GET Button.js').wrap(request3903)

request3904 = HTTPRequest(url=url0, headers=headers13)
request3904 = Test(3904, 'GET jqueryMultiSelect.js').wrap(request3904)

request3905 = HTTPRequest(url=url0, headers=headers13)
request3905 = Test(3905, 'GET PopulationHierarchyBrowser.js').wrap(request3905)

request3906 = HTTPRequest(url=url0, headers=headers13)
request3906 = Test(3906, 'GET PopulationHierarchyBrowserData.js').wrap(request3906)

request3907 = HTTPRequest(url=url0, headers=headers13)
request3907 = Test(3907, 'GET PopulationHierarchyBrowserUI.js').wrap(request3907)

request3908 = HTTPRequest(url=url0, headers=headers13)
request3908 = Test(3908, 'GET AssignmentCreator.js').wrap(request3908)

request3909 = HTTPRequest(url=url0, headers=headers13)
request3909 = Test(3909, 'GET AssignmentViewer.js').wrap(request3909)

request3910 = HTTPRequest(url=url0, headers=headers13)
request3910 = Test(3910, 'GET MyAssignmentsPage.js').wrap(request3910)

request4001 = HTTPRequest(url=url0, headers=headers9)
request4001 = Test(4001, 'GET list').wrap(request4001)

request4101 = HTTPRequest(url=url0, headers=headers9)
request4101 = Test(4101, 'GET create').wrap(request4101)

request4102 = HTTPRequest(url=url0, headers=headers13)
request4102 = Test(4102, 'GET sharing.js').wrap(request4102)

request4103 = HTTPRequest(url=url0, headers=headers13)
request4103 = Test(4103, 'GET SharingDropdown.js').wrap(request4103)

request4201 = HTTPRequest(url=url0, headers=headers12)
request4201 = Test(4201, 'POST base').wrap(request4201)

request4202 = HTTPRequest(url=url0, headers=headers13)
request4202 = Test(4202, 'GET Ajax.js').wrap(request4202)

request4203 = HTTPRequest(url=url0, headers=headers13)
request4203 = Test(4203, 'GET Button.js').wrap(request4203)

request4204 = HTTPRequest(url=url0, headers=headers13)
request4204 = Test(4204, 'GET jqueryMultiSelect.js').wrap(request4204)

request4205 = HTTPRequest(url=url0, headers=headers13)
request4205 = Test(4205, 'GET PopulationHierarchyBrowser.js').wrap(request4205)

request4206 = HTTPRequest(url=url0, headers=headers13)
request4206 = Test(4206, 'GET PopulationHierarchyBrowserData.js').wrap(request4206)

request4207 = HTTPRequest(url=url0, headers=headers13)
request4207 = Test(4207, 'GET PopulationHierarchyBrowserUI.js').wrap(request4207)

request4208 = HTTPRequest(url=url0, headers=headers13)
request4208 = Test(4208, 'GET AssignmentCreator.js').wrap(request4208)

request4209 = HTTPRequest(url=url0, headers=headers13)
request4209 = Test(4209, 'GET AssignmentViewer.js').wrap(request4209)

request4210 = HTTPRequest(url=url0, headers=headers13)
request4210 = Test(4210, 'GET MyAssignmentsPage.js').wrap(request4210)

request4301 = HTTPRequest(url=url0, headers=headers9)
request4301 = Test(4301, 'GET list').wrap(request4301)

request4401 = HTTPRequest(url=url0, headers=headers9)
request4401 = Test(4401, 'GET create').wrap(request4401)

request4402 = HTTPRequest(url=url0, headers=headers13)
request4402 = Test(4402, 'GET sharing.js').wrap(request4402)

request4403 = HTTPRequest(url=url0, headers=headers13)
request4403 = Test(4403, 'GET SharingDropdown.js').wrap(request4403)

# going to create item
request4501 = HTTPRequest(url=url0, headers=headers16)
request4501 = Test(4501, 'GET create').wrap(request4501)

request4502 = HTTPRequest(url=url0, headers=headers32)
request4502 = Test(4502, 'GET create.css').wrap(request4502)

request4503 = HTTPRequest(url=url0, headers=headers33)
request4503 = Test(4503, 'GET icon_view_detail.png').wrap(request4503)

request4504 = HTTPRequest(url=url0, headers=headers34)
request4504 = Test(4504, 'GET slider_sprite.png').wrap(request4504)

request4505 = HTTPRequest(url=url0, headers=headers35)
request4505 = Test(4505, 'GET locate_tab_arrows.png').wrap(request4505)

request4506 = HTTPRequest(url=url0, headers=headers32)
request4506 = Test(4506, 'GET CollapsibleBox.css').wrap(request4506)

request4507 = HTTPRequest(url=url0, headers=headers34)
request4507 = Test(4507, 'GET create_box_bottom_connector.png').wrap(request4507)

request4508 = HTTPRequest(url=url0, headers=headers32)
request4508 = Test(4508, 'GET create_item.css').wrap(request4508)

request4509 = HTTPRequest(url=url0, headers=headers33)
request4509 = Test(4509, 'GET mc_delete.png').wrap(request4509)

request4510 = HTTPRequest(url=url0, headers=headers34)
request4510 = Test(4510, 'GET create_box_top_connector.png').wrap(request4510)

request4511 = HTTPRequest(url=url0, headers=headers36)
request4511 = Test(4511, 'GET CollapsibleBox.js').wrap(request4511)

request4512 = HTTPRequest(url=url0, headers=headers36)
request4512 = Test(4512, 'GET collapsible_panel.js').wrap(request4512)

request4513 = HTTPRequest(url=url0, headers=headers36)
request4513 = Test(4513, 'GET GradeRangeSlider.js').wrap(request4513)

request4514 = HTTPRequest(url=url0, headers=headers36)
request4514 = Test(4514, 'GET TimeSlider.js').wrap(request4514)

request4515 = HTTPRequest(url=url0, headers=headers36)
request4515 = Test(4515, 'GET AlignableItemBankEntity.js').wrap(request4515)

request4516 = HTTPRequest(url=url0, headers=headers36)
request4516 = Test(4516, 'GET Item.js').wrap(request4516)

request4517 = HTTPRequest(url=url0, headers=headers36)
request4517 = Test(4517, 'GET LinkedPassage.js').wrap(request4517)

request4518 = HTTPRequest(url=url0, headers=headers36)
request4518 = Test(4518, 'GET LinkedRubrics.js').wrap(request4518)

request4519 = HTTPRequest(url=url0, headers=headers36)
request4519 = Test(4519, 'GET OpenResponseScoring.js').wrap(request4519)

request4520 = HTTPRequest(url=url0, headers=headers36)
request4520 = Test(4520, 'GET EditReady.js').wrap(request4520)

request4521 = HTTPRequest(url=url0, headers=headers37)
request4521 = Test(4521, 'GET standards_puffy_cookie_crumb.png').wrap(request4521)

request4601 = HTTPRequest(url=url0, headers=headers38)
request4601 = Test(4601, 'GET standardsTree').wrap(request4601)

request4701 = HTTPRequest(url=url0, headers=headers38)
request4701 = Test(4701, 'GET standardsTree').wrap(request4701)

request4801 = HTTPRequest(url=url0, headers=headers38)
request4801 = Test(4801, 'GET standardsTree').wrap(request4801)

request4901 = HTTPRequest(url=url0, headers=headers38)
request4901 = Test(4901, 'GET standardsTree').wrap(request4901)

request5001 = HTTPRequest(url=url0, headers=headers38)
request5001 = Test(5001, 'GET standardsTree').wrap(request5001)

request5101 = HTTPRequest(url=url0, headers=headers38)
request5101 = Test(5101, 'GET standardsTree').wrap(request5101)

request5102 = HTTPRequest(url=url0, headers=headers39)
request5102 = Test(5102, 'GET slider.png').wrap(request5102)

request5103 = HTTPRequest(url=url0, headers=headers33)
request5103 = Test(5103, 'GET btn_section_expander_item.png').wrap(request5103)

request5104 = HTTPRequest(url=url0, headers=headers33)
request5104 = Test(5104, 'GET btn_section_expander_item_closed.png').wrap(request5104)

request5201 = HTTPRequest(url=url0, headers=headers38)
request5201 = Test(5201, 'GET standardsTreeGrandkids').wrap(request5201)

request5301 = HTTPRequest(url=url0, headers=headers38)
request5301 = Test(5301, 'GET standardsTreeGrandkids').wrap(request5301)

request5302 = HTTPRequest(url=url0, headers=headers37)
request5302 = Test(5302, 'GET icon_caret_blue_down.png').wrap(request5302)

request5303 = HTTPRequest(url=url0, headers=headers33)
request5303 = Test(5303, 'GET btn_radio.png').wrap(request5303)

request5304 = HTTPRequest(url=url0, headers=headers35)
request5304 = Test(5304, 'GET mc_box_inner_top.gif').wrap(request5304)

request5305 = HTTPRequest(url=url0, headers=headers35)
request5305 = Test(5305, 'GET mc_arranger_buttons.png').wrap(request5305)

request5306 = HTTPRequest(url=url0, headers=headers35)
request5306 = Test(5306, 'GET mc_box_inner_bottom.gif').wrap(request5306)

request5307 = HTTPRequest(url=url0, headers=headers36)
request5307 = Test(5307, 'GET en.js').wrap(request5307)

request5308 = HTTPRequest(url=url0, headers=headers36)
request5308 = Test(5308, 'GET editor_template.js').wrap(request5308)

request5309 = HTTPRequest(url=url0, headers=headers36)
request5309 = Test(5309, 'GET editor_plugin.js').wrap(request5309)

request5310 = HTTPRequest(url=url0, headers=headers36)
request5310 = Test(5310, 'GET editor_plugin.js').wrap(request5310)

request5311 = HTTPRequest(url=url0, headers=headers36)
request5311 = Test(5311, 'GET editor_plugin.js').wrap(request5311)

request5312 = HTTPRequest(url=url0, headers=headers36)
request5312 = Test(5312, 'GET editor_plugin.js').wrap(request5312)

request5313 = HTTPRequest(url=url0, headers=headers36)
request5313 = Test(5313, 'GET editor_plugin.js').wrap(request5313)

request5314 = HTTPRequest(url=url0, headers=headers36)
request5314 = Test(5314, 'GET editor_plugin.js').wrap(request5314)

request5315 = HTTPRequest(url=url0, headers=headers36)
request5315 = Test(5315, 'GET editor_plugin.js').wrap(request5315)

request5316 = HTTPRequest(url=url0, headers=headers36)
request5316 = Test(5316, 'GET en.js').wrap(request5316)

request5317 = HTTPRequest(url=url0, headers=headers36)
request5317 = Test(5317, 'GET editor_plugin.js').wrap(request5317)

request5318 = HTTPRequest(url=url0, headers=headers36)
request5318 = Test(5318, 'GET editor_plugin.js').wrap(request5318)

request5319 = HTTPRequest(url=url0, headers=headers36)
request5319 = Test(5319, 'GET editor_plugin.js').wrap(request5319)

request5320 = HTTPRequest(url=url0, headers=headers32)
request5320 = Test(5320, 'GET ui.css').wrap(request5320)

request5321 = HTTPRequest(url=url0, headers=headers32)
request5321 = Test(5321, 'GET ui_threetwelve.css').wrap(request5321)

request5322 = HTTPRequest(url=url0, headers=headers32)
request5322 = Test(5322, 'GET window.css').wrap(request5322)

request5323 = HTTPRequest(url=url0, headers=headers32)
request5323 = Test(5323, 'GET content.css').wrap(request5323)

request5324 = HTTPRequest(url=url0, headers=headers40)
request5324 = Test(5324, 'GET icons.gif').wrap(request5324)

request5325 = HTTPRequest(url=url0, headers=headers40)
request5325 = Test(5325, 'GET button_bg.png').wrap(request5325)

request5326 = HTTPRequest(url=url0, headers=headers41)
request5326 = Test(5326, 'GET small.png').wrap(request5326)

request5327 = HTTPRequest(url=url0, headers=headers41)
request5327 = Test(5327, 'GET medium.png').wrap(request5327)

request5328 = HTTPRequest(url=url0, headers=headers41)
request5328 = Test(5328, 'GET btn_wysiwyg_add_space_unruled.png').wrap(request5328)

request5329 = HTTPRequest(url=url0, headers=headers41)
request5329 = Test(5329, 'GET large.png').wrap(request5329)

request5330 = HTTPRequest(url=url0, headers=headers41)
request5330 = Test(5330, 'GET ed_mathformula.gif').wrap(request5330)

request5331 = HTTPRequest(url=url0, headers=headers41)
request5331 = Test(5331, 'GET btn_wysiwyg_space_title_1.gif').wrap(request5331)

request5332 = HTTPRequest(url=url0, headers=headers41)
request5332 = Test(5332, 'GET btn_wysiwyg_space_title_2.gif').wrap(request5332)

request5333 = HTTPRequest(url=url0, headers=headers41)
request5333 = Test(5333, 'GET btn_wysiwyg_space_title_3.gif').wrap(request5333)

request5334 = HTTPRequest(url=url0, headers=headers41)
request5334 = Test(5334, 'GET btn_wysiwyg_add_space_ruled.png').wrap(request5334)

request5401 = HTTPRequest(url=url0, headers=headers36)
request5401 = Test(5401, 'GET manage').wrap(request5401)

request5402 = HTTPRequest(url=url0, headers=headers33)
request5402 = Test(5402, 'GET red_cancel_icon.png').wrap(request5402)

request5403 = HTTPRequest(url=url0, headers=headers42)
request5403 = Test(5403, 'GET left_pane_background.png').wrap(request5403)

request5404 = HTTPRequest(url=url0, headers=headers33)
request5404 = Test(5404, 'GET search_within_bttn.png').wrap(request5404)

request5405 = HTTPRequest(url=url0, headers=headers43)
request5405 = Test(5405, 'GET ViewItemBankEntity.js').wrap(request5405)

request5406 = HTTPRequest(url=url0, headers=headers42)
request5406 = Test(5406, 'GET search_within_glass.png').wrap(request5406)

request5407 = HTTPRequest(url=url0, headers=headers43)
request5407 = Test(5407, 'GET sharing.js').wrap(request5407)

request5408 = HTTPRequest(url=url0, headers=headers42)
request5408 = Test(5408, 'GET locate_stroke_quantity_results_bg.png').wrap(request5408)

request5409 = HTTPRequest(url=url0, headers=headers43)
request5409 = Test(5409, 'GET createStandardsUi.js').wrap(request5409)

request5410 = HTTPRequest(url=url0, headers=headers43)
request5410 = Test(5410, 'GET viewStandardsUi.js').wrap(request5410)

request5411 = HTTPRequest(url=url0, headers=headers43)
request5411 = Test(5411, 'GET tooltip.js').wrap(request5411)

request5412 = HTTPRequest(url=url0, headers=headers43)
request5412 = Test(5412, 'GET AssignmentCreator.js').wrap(request5412)

request5413 = HTTPRequest(url=url0, headers=headers43)
request5413 = Test(5413, 'GET EntityPopupSourceUI.js').wrap(request5413)

request5414 = HTTPRequest(url=url0, headers=headers43)
request5414 = Test(5414, 'GET ManageBrowser.js').wrap(request5414)

request5415 = HTTPRequest(url=url0, headers=headers43)
request5415 = Test(5415, 'GET ManageBrowserRenderer.js').wrap(request5415)

request5416 = HTTPRequest(url=url0, headers=headers43)
request5416 = Test(5416, 'GET ManageRubricBrowserRenderer.js').wrap(request5416)

request5417 = HTTPRequest(url=url0, headers=headers43)
request5417 = Test(5417, 'GET ManageStandardsUi.js').wrap(request5417)

request5418 = HTTPRequest(url=url0, headers=headers43)
request5418 = Test(5418, 'GET AssessmentFilterWidget.js').wrap(request5418)

request5419 = HTTPRequest(url=url0, headers=headers43)
request5419 = Test(5419, 'GET ManageFilterWidget.js').wrap(request5419)

request5420 = HTTPRequest(url=url0, headers=headers43)
request5420 = Test(5420, 'GET QuestionType.js').wrap(request5420)

request5421 = HTTPRequest(url=url0, headers=headers43)
request5421 = Test(5421, 'GET OpenResponseQuestionType.js').wrap(request5421)

request5422 = HTTPRequest(url=url0, headers=headers43)
request5422 = Test(5422, 'GET SubjectDropdown.js').wrap(request5422)

request5423 = HTTPRequest(url=url0, headers=headers43)
request5423 = Test(5423, 'GET EditPageSubjectDropdown.js').wrap(request5423)

request5424 = HTTPRequest(url=url0, headers=headers43)
request5424 = Test(5424, 'GET jqueryMultiSelect.js').wrap(request5424)

request5425 = HTTPRequest(url=url0, headers=headers43)
request5425 = Test(5425, 'GET manage_ready.js').wrap(request5425)

request5501 = HTTPRequest(url=url0, headers=headers38)
request5501 = Test(5501, 'GET myStandardsRootNodes').wrap(request5501)

request5601 = HTTPRequest(url=url0, headers=headers38)
request5601 = Test(5601, 'GET getAll').wrap(request5601)

request5602 = HTTPRequest(url=url0, headers=headers42)
request5602 = Test(5602, 'GET standards_bullet_image.png').wrap(request5602)

request5701 = HTTPRequest(url=url0, headers=headers36)
request5701 = Test(5701, 'GET renderRubricOverview').wrap(request5701)

request5801 = HTTPRequest(url=url0, headers=headers44)
request5801 = Test(5801, 'POST items').wrap(request5801)

request5901 = HTTPRequest(url=url0, headers=headers45)
request5901 = Test(5901, 'POST sharingAgreement').wrap(request5901)

request6001 = HTTPRequest(url=url0, headers=headers44)
request6001 = Test(6001, 'POST saveDraft').wrap(request6001)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET login (requests 101-181)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request101.GET('/oib/login')

    grinder.sleep(18)
    request102.GET('/oib/home')

    grinder.sleep(1171)
    request103.GET('/oib/static/common/css/widgets/GlobalNavBar.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(19)
    request104.GET('/oib/static/common/css/widgets/mClassNavBar.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(26)
    request105.GET('/oib/static/css/jquery-ui-1.7.2.custom.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    grinder.sleep(72)
    request106.GET('/oib/static/common/css/basic.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request107.GET('/oib/static/common/css/skin.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request108.GET('/oib/static/css/styled_text.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request109.GET('/oib/static/css/standards.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request110.GET('/oib/static/css/widgets/help.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request111.GET('/oib/static/common/images/mclass/logo_mclass_navbar.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(25)
    request112.GET('/oib/static/common/images/mclass/px.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request113.GET('/oib/static/common/images/icon_question_contextual.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(14)
    request114.GET('/oib/static/images/navigation/navbar_logo.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request115.GET('/oib/static/images/navigation/navigation_buttons_sprite.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request116.GET('/oib/static/images/navigation/navigation_buttons_icons_sprite.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request117.GET('/oib/static/images/assessment/assess_back.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request118.GET('/oib/static/css/manage/manage.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request119.GET('/oib/static/css/manage/manage_item.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request120.GET('/oib/static/css/manage/manage_passage.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request121.GET('/oib/static/css/dashboard.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request122.GET('/oib/static/css/manage/manage_rubric.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request123.GET('/oib/static/css/manage/manage_assessment.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request124.GET('/oib/static/images/table_contents_bottom_tile.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request125.GET('/oib/static/common/css/3p/jqueryMultiSelect.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request126.GET('/oib/static/css/view_entity.css', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request127.GET('/oib/static/images/table_contents_right_tile.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request128.GET('/oib/static/images/sprites/body_content_area_corner_sprite.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request129.GET('/oib/static/images/sprites/table_contents_corners_sprite.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request130.GET('/oib/static/images/ajax-loader-lrg.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request131.GET('/oib/static/common/js/3p/closure.base.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(56)
    request132.GET('/oib/static/images/dashboard/video_box_gradient.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request133.GET('/oib/static/common/js/3p/jquery-1.3.2.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(34)
    request134.GET('/oib/static/common/js/3p/jqueryui/ui.core.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(1463)
    request135.GET('/oib/static/common/js/3p/jqueryui/ui.draggable.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(28)
    request136.GET('/oib/static/common/js/3p/jqueryui/ui.sortable.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request137.GET('/oib/static/common/images/mclass/bg_header_blue_dot.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request138.GET('/oib/static/common/js/3p/jqueryui/ui.resizable.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(35)
    request139.GET('/oib/static/common/js/3p/jqueryui/ui.slider.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request140.GET('/oib/static/common/js/3p/jqueryui/ui.dialog.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request141.GET('/oib/static/common/js/3p/jqueryui/ui.tabs.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request142.GET('/oib/static/common/js/jquery_setup.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request143.GET('/oib/static/common/js/3p/prototype.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(37)
    request144.GET('/oib/static/common/js/3p/jquery.form.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request145.GET('/oib/static/common/js/3p/jquery.tooltip.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request146.GET('/oib/static/common/js/3p/autoresize.jquery.min.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request147.GET('/oib/static/common/js/3p/jsonStringify.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request148.GET('/oib/static/images/top_bar_divider.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request149.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/js/LaTeXMathML.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(14)
    request150.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/js/math-utilities.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request151.GET('/oib/static/js/standardsBrowser/standardsUi.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request152.GET('/oib/static/js/standardsBrowser/standards.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    grinder.sleep(15)
    request153.GET('/oib/static/common/js/widgets/BackspaceSuppress.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request154.GET('/oib/static/common/js/widgets/TimeoutDetect.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request155.GET('/oib/static/js/global_ready.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request156.GET('/oib/static/js/wgen.oib.utilities.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request157.GET('/oib/static/common/js/3p/RoboHelp_CSH.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request158.GET('/oib/static/common/js/widgets/help.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request159.GET('/oib/static/js/jquery_functions.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request160.GET('/oib/static/js/cookieHandler.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(118)
    request161.GET('/oib/static/common/js/3p/googleAnalytics.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request162.GET('/oib/static/js/ViewItemBankEntity.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request163.GET('/oib/static/js/widgets/sharing.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request164.GET('/oib/static/js/standardsBrowser/createStandardsUi.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request165.GET('/oib/static/js/standardsBrowser/viewStandardsUi.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request166.GET('/oib/static/js/widgets/SharingDropdown.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request167.GET('/oib/static/common/js/3p/jqueryMultiSelect.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(11)
    request168.GET('/oib/static/js/widgets/tooltip.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request169.GET('/oib/static/js/EntityPopupSourceUI.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request170.GET('/oib/static/js/manage/ManageBrowser.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    grinder.sleep(18)
    request171.GET('/oib/static/js/manage/ManageBrowserRenderer.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request172.GET('/oib/static/js/manage/ManageItemBrowserRenderer.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request173.GET('/oib/static/js/manage/ManagePassageBrowserRenderer.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request174.GET('/oib/static/js/manage/ManageRubricBrowserRenderer.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request175.GET('/oib/static/js/manage/ManageAssessmentBrowserRenderer.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request176.GET('/oib/static/js/dashboard/widgets/RecentEntityWidget.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request177.GET('/oib/static/js/dashboard/DashboardPage.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request178.GET('/oib/static/js/dashboard/dashboard_ready.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request179.GET('/oib/static/js/item/question/QuestionType.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request180.GET('/oib/static/js/item/question/OpenResponseQuestionType.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    request181.GET('/oib/static/common/js/widgets/GlobalNavBar.js', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    return result

  def page2(self):
    """GET recent (requests 201-202)."""
    self.token_type = \
      'all'
    self.token_pageSize = \
      '50'
    self.token_page = \
      '0'
    self.token__ = \
      '1293559099086'
    result = request201.GET('/oib/webservices/entities/recent' +
      '?type=' +
      self.token_type +
      '&pageSize=' +
      self.token_pageSize +
      '&page=' +
      self.token_page +
      '&_=' +
      self.token__)

    request202.GET('/oib/static/images/buttons/blue_button_flat.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    return result

  def page3(self):
    """GET ellipsis.xml (requests 301-306)."""
    result = request301.GET('/oib/static/common/css/ellipsis.xml', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:07 GMT'), ))

    grinder.sleep(29)
    request302.GET('/oib/static/images/manage/locate_rounded_corner_objects.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request303.GET('/oib/static/images/view_overlay/sprites.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request304.GET('/oib/static/images/manage/assessment_item_count_box.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    grinder.sleep(35406)
    request305.GET('/oib/static/images/view_overlay/border.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    grinder.sleep(290)
    request306.GET('/oib/static/images/view_overlay/close_X.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    return result

  def page4(self):
    """POST base (requests 401-415)."""
    result = request401.POST('/oib/assessment/view/base',
      ( NVPair('id', '342'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    grinder.sleep(262)
    request402.GET('/oib/static/images/view_overlay/icon_edit.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request403.GET('/oib/static/images/view_overlay/icon_delete.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    grinder.sleep(72)
    self.token__ = \
      '1293559137702'
    request404.GET('/oib/static/common/js/wgen/threetwelve/Ajax.js' +
      '?_=' +
      self.token__)

    grinder.sleep(43)
    self.token__ = \
      '1293559137845'
    request405.GET('/oib/static/common/js/widgets/Button.js' +
      '?_=' +
      self.token__)

    grinder.sleep(147)
    request406.GET('/oib/static/images/view_overlay/icon_cloneAndEdit.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    self.token__ = \
      '1293559137886'
    request407.GET('/oib/static/common/js/3p/jqueryMultiSelect.js' +
      '?_=' +
      self.token__)

    grinder.sleep(170)
    self.token__ = \
      '1293559138287'
    request408.GET('/oib/static/js/widgets/PopulationHierarchyBrowser.js' +
      '?_=' +
      self.token__)

    request409.GET('/oib/static/images/view_overlay/icon_print.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    self.token__ = \
      '1293559138320'
    request410.GET('/oib/static/js/widgets/PopulationHierarchyBrowserData.js' +
      '?_=' +
      self.token__)

    request411.GET('/oib/static/images/tooltips/tooltip_win_arrow_top.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    self.token__ = \
      '1293559138334'
    request412.GET('/oib/static/js/widgets/PopulationHierarchyBrowserUI.js' +
      '?_=' +
      self.token__)

    grinder.sleep(17)
    self.token__ = \
      '1293559138380'
    request413.GET('/oib/static/js/widgets/AssignmentCreator.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1293559138397'
    request414.GET('/oib/static/js/widgets/AssignmentViewer.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1293559138427'
    request415.GET('/oib/static/js/assignment/MyAssignmentsPage.js' +
      '?_=' +
      self.token__)

    return result

  def page5(self):
    """GET list (request 501)."""
    self.token_assessmentId = \
      '31'
    self.token__ = \
      '1293559138444'
    result = request501.GET('/oib/assignment/list' +
      '?assessmentId=' +
      self.token_assessmentId +
      '&_=' +
      self.token__)

    return result

  def page6(self):
    """GET create (requests 601-611)."""
    self.token__ = \
      '1293559138445'
    result = request601.GET('/oib/assignment/create' +
      '?_=' +
      self.token__ +
      '&assessmentId=' +
      self.token_assessmentId)

    self.token__ = \
      '1293559138447'
    request602.GET('/oib/static/js/widgets/sharing.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1293559138499'
    request603.GET('/oib/static/js/widgets/SharingDropdown.js' +
      '?_=' +
      self.token__)

    grinder.sleep(40)
    request604.GET('/oib/static/images/view_overlay/overview_vert.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request605.GET('/oib/static/images/view_overlay/overview_tr.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request606.GET('/oib/static/images/view_overlay/overview_tl.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request607.GET('/oib/static/images/view_overlay/overview_horiz.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    grinder.sleep(37)
    request608.GET('/oib/static/images/assessment/rounded_corner_yellow_top.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    grinder.sleep(32)
    request609.GET('/oib/static/images/assignment/icon_assignment.gif', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    request610.GET('/oib/static/images/assessment/rounded_corner_yellow_horiz_bg.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    grinder.sleep(51)
    request611.GET('/oib/static/images/assessment/rounded_corner_yellow_vert_bg.png', None,
      ( NVPair('If-Modified-Since', 'Wed, 12 Jan 2011 03:29:06 GMT'), ))

    return result

  def page7(self):
    """GET clone (request 701)."""
    self.token_id = \
      '342'
    result = request701.GET('/oib/assessment/clone' +
      '?id=' +
      self.token_id)

    return result

  def page8(self):
    """POST sharingAgreement (request 801)."""
    result = request801.POST('/oib/sharingAgreement',
      '',
      ( NVPair('Content-Type', 'application/xml; charset=UTF-8'), ))

    return result

  def page9(self):
    """GET keepalive (request 901)."""
    self.token__ = \
      '1293559206153'
    result = request901.GET('/oib/keepalive' +
      '?_=' +
      self.token__)

    return result

  def page10(self):
    """POST downloads (request 1001)."""
    self.token_client = \
      'navclient-auto-ffox'
    self.token_appver = \
      '3.0.14'
    self.token_pver = \
      '2.2'
    self.token_wrkey = \
      'AKEgNiuTtIIXjlzTHwJWR3w1vmvaVRuoKEhzd8szLOCRlYMaMYHGByBWovnnw2RrxtKtnEmLdxpj5hQgiiwCE2lKsMfDe621Mw=='
    result = request1001.POST('/safebrowsing/downloads' +
      '?client=' +
      self.token_client +
      '&appver=' +
      self.token_appver +
      '&pver=' +
      self.token_pver +
      '&wrkey=' +
      self.token_wrkey,
      '''goog-malware-shavar;a:25921-26610,27841-29825:s:38401-43630:mac\ngoog-phish-shavar;a:121971-126579:s:64608-65894:mac\n''',
      ( NVPair('Content-Type', 'text/plain'), ))

    return result

  def page11(self):
    """GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAEY79QCIPjUAioGcKoAAP8BMgVvqgAAAQ (request 1101)."""
    result = request1101.GET('/safebrowsing/rd/ChNnb29nLW1hbHdhcmUtc2hhdmFyEAEY79QCIPjUAioGcKoAAP8BMgVvqgAAAQ')

    return result

  def page12(self):
    """GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYodgBIMDZATIZIWwAAP____-__7f7v_____3____f__7_AA (request 1201)."""
    result = request1201.GET('/safebrowsing/rd/ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYodgBIMDZATIZIWwAAP____-__7f7v_____3____f__7_AA')

    return result

  def page13(self):
    """GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYwegBIIDrATItQXQAAP_v_______v_9______7______vv___9____9_v7_7_9__-_9____cA (request 1301)."""
    result = request1301.GET('/safebrowsing/rd/ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYwegBIIDrATItQXQAAP_v_______v_9______7______vv___9____9_v7_7_9__-_9____cA')

    return result

  def page14(self):
    """GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYgesBIMDtATItgXUAAP3__-_____9___v______-______________3___________v6__78A (request 1401)."""
    result = request1401.GET('/safebrowsing/rd/ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYgesBIMDtATItgXUAAP3__-_____9___v______-______________3___________v6__78A')

    return result

  def page15(self):
    """GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYwe0BIIDwATItwXYAAP____v___d_3____vf7_f_____7__________________________8A (request 1501)."""
    result = request1501.GET('/safebrowsing/rd/ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYwe0BIIDwATItwXYAAP____v___d_3____vf7_f_____7__________________________8A')

    return result

  def page16(self):
    """GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYgfABIICEAiqoAuR4AAD___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________8fMiEBeAAA_7_ff_9______________________________wc (request 1601)."""
    result = request1601.GET('/safebrowsing/rd/ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYgfABIICEAiqoAuR4AAD___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________8fMiEBeAAA_7_ff_9______________________________wc')

    return result

  def page17(self):
    """GET ChFnb29nLXBoaXNoLXNoYXZhchABGLGCBCCAgwQyDzEBAQD_____-_______AA (request 1701)."""
    result = request1701.GET('/safebrowsing/rd/ChFnb29nLXBoaXNoLXNoYXZhchABGLGCBCCAgwQyDzEBAQD_____-_______AA')

    return result

  def page18(self):
    """GET ChFnb29nLXBoaXNoLXNoYXZhchABGIGDBCCAiAQyVYEBAQD___9________________________________3_____________________________________________________________________wA (request 1801)."""
    result = request1801.GET('/safebrowsing/rd/ChFnb29nLXBoaXNoLXNoYXZhchABGIGDBCCAiAQyVYEBAQD___9________________________________3_____________________________________________________________________wA')

    return result

  def page19(self):
    """POST save (request 1901)."""
    result = request1901.POST('/oib/assessment/save',
      ( NVPair('assessmentJSON', '{\"subject\": \"ELA\", \"title\": \"Clone of: AssessmentMixedOrFallsOffPage\", \"type\": \"ad_hoc\", \"delivery\": \"offline\", \"body\": {\"main_content\": [{\"type\": \"booklet\", \"title\": \"\", \"children\": [{\"type\": \"item\", \"vcid\": \"331\", \"version\": \"1\", \"entity_id\": \"259\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}, {\"type\": \"item\", \"vcid\": \"332\", \"version\": \"1\", \"entity_id\": \"260\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}, {\"type\": \"item\", \"vcid\": \"333\", \"version\": \"1\", \"entity_id\": \"261\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}, {\"type\": \"item\", \"vcid\": \"334\", \"version\": \"1\", \"entity_id\": \"262\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}, {\"type\": \"item\", \"vcid\": \"335\", \"version\": \"1\", \"entity_id\": \"263\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}, {\"type\": \"item\", \"vcid\": \"336\", \"version\": \"1\", \"entity_id\": \"264\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}, {\"type\": \"item\", \"vcid\": \"337\", \"version\": \"1\", \"entity_id\": \"265\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}, {\"type\": \"item\", \"vcid\": \"338\", \"version\": \"1\", \"entity_id\": \"266\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}, {\"type\": \"item\", \"vcid\": \"339\", \"version\": \"1\", \"entity_id\": \"267\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}, {\"type\": \"item\", \"vcid\": \"340\", \"version\": \"1\", \"entity_id\": \"268\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}, {\"type\": \"item\", \"vcid\": \"341\", \"version\": \"1\", \"entity_id\": \"269\", \"selectedRubricStandards\": {}, \"standard\": \"51848\"}]}]}}'),
        NVPair('subject', 'ELA'),
        NVPair('ctoken', 'bzxXnCSP'),
        NVPair('poolId', '463'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page20(self):
    """GET view (requests 2001-2074)."""
    result = request2001.GET('/outcomes/report/view')

    grinder.sleep(388)
    request2002.GET('/outcomes/static/common/css/basic.css')

    grinder.sleep(39)
    request2003.GET('/outcomes/static/common/css/skin.css')

    request2004.GET('/outcomes/static/common/css/widgets/GlobalNavBar.css')

    grinder.sleep(11)
    request2005.GET('/outcomes/static/css/jquery-ui-1.7.2.custom.css')

    request2006.GET('/outcomes/static/common/css/widgets/mClassNavBar.css')

    grinder.sleep(47)
    request2007.GET('/outcomes/static/common/images/mclass/logo_mclass_navbar.gif')

    request2008.GET('/outcomes/static/common/images/icon_question_contextual.gif')

    request2009.GET('/outcomes/static/common/images/mclass/px.gif')

    request2010.GET('/outcomes/static/css/reports.css')

    request2011.GET('/outcomes/static/css/matrix.css')

    request2012.GET('/outcomes/static/css/learning_map_legend.css')

    request2013.GET('/outcomes/static/css/learning_map.css')

    request2014.GET('/outcomes/static/css/ellipsis.css')

    grinder.sleep(22)
    request2015.GET('/outcomes/static/css/widgets/featheredBox.css')

    request2016.GET('/outcomes/static/images/navigation/navbar_logo.gif')

    request2017.GET('/outcomes/static/css/widgets/buttonBar.css')

    request2018.GET('/outcomes/static/js/hexmap/assets/honeycomb.css')

    request2019.GET('/outcomes/static/css/overlay/item_analysis.css')

    request2020.GET('/outcomes/static/css/overlay/standard_analysis.css')

    request2021.GET('/outcomes/static/js/3p/closure.base.js')

    grinder.sleep(44)
    request2022.GET('/outcomes/static/images/learningMap/feathered_box_vert.png')

    request2023.GET('/outcomes/static/images/learningMap/feathered_box_horiz.png')

    request2024.GET('/outcomes/static/images/learningMap/feathered_box.png')

    grinder.sleep(45)
    request2025.GET('/outcomes/static/images/button_gel.png')

    grinder.sleep(163)
    request2026.GET('/outcomes/static/css/widgets/dropdownControl.css')

    request2027.GET('/outcomes/static/css/report_colors.css')

    grinder.sleep(26)
    request2028.GET('/outcomes/static/js/3p/jquery-1.3.2.js')

    grinder.sleep(148)
    request2029.GET('/outcomes/static/js/3p/jqueryui/ui.core.js')

    grinder.sleep(15)
    request2030.GET('/outcomes/static/js/3p/jqueryui/ui.draggable.js')

    grinder.sleep(15)
    request2031.GET('/outcomes/static/js/3p/jqueryui/ui.sortable.js')

    grinder.sleep(52)
    request2032.GET('/outcomes/static/js/3p/jqueryui/ui.resizable.js')

    grinder.sleep(15)
    request2033.GET('/outcomes/static/js/3p/jqueryui/ui.slider.js')

    request2034.GET('/outcomes/static/js/3p/jqueryui/ui.dialog.js')

    grinder.sleep(89)
    request2035.GET('/outcomes/static/js/3p/jqueryui/ui.tabs.js')

    grinder.sleep(13)
    request2036.GET('/outcomes/static/js/jquery_functions.js')

    grinder.sleep(29)
    request2037.GET('/outcomes/static/js/jquery_setup.js')

    request2038.GET('/outcomes/static/js/3p/prototype.js')

    grinder.sleep(62)
    request2039.GET('/outcomes/static/js/3p/jquery.form.js')

    grinder.sleep(54)
    request2040.GET('/outcomes/static/js/3p/autoresize.jquery.min.js')

    grinder.sleep(13)
    request2041.GET('/outcomes/static/js/3p/jquery.tooltip.js')

    request2042.GET('/outcomes/static/common/js/widgets/BackspaceSuppress.js')

    request2043.GET('/outcomes/static/common/js/widgets/TimeoutDetect.js')

    request2044.GET('/outcomes/static/js/global_ready.js')

    request2045.GET('/outcomes/static/js/wgen.oib.utilities.js')

    request2046.GET('/outcomes/static/common/js/3p/RoboHelp_CSH.js')

    grinder.sleep(46)
    request2047.GET('/outcomes/static/common/js/widgets/help.js')

    request2048.GET('/outcomes/static/js/cookieHandler.js')

    grinder.sleep(17)
    request2049.GET('/outcomes/static/common/js/3p/googleAnalytics.js')

    grinder.sleep(102)
    request2050.GET('/outcomes/static/js/widgets/DropdownControl.js')

    request2051.GET('/outcomes/static/js/widgets/ClasseAndAssessmentDropdownPicker.js')

    request2052.GET('/outcomes/static/js/widgets/ClasseAndAssessmentDropdownPickerData.js')

    request2053.GET('/outcomes/static/js/widgets/ButtonBar.js')

    request2054.GET('/outcomes/static/js/hexmap/js/HoneycombWidgetUI.js')

    request2055.GET('/outcomes/static/js/hexmap/js/HoneycombEvent.js')

    request2056.GET('/outcomes/static/js/hexmap/js/TileManager.js')

    grinder.sleep(51)
    request2057.GET('/outcomes/static/js/hexmap/js/TileManagerUtil.js')

    request2058.GET('/outcomes/static/js/hexmap/js/HoneycombWidget.js')

    request2059.GET('/outcomes/static/js/hexmap/js/LearningMapUtil.js')

    request2060.GET('/outcomes/static/js/hexmap/js/Config.js')

    request2061.GET('/outcomes/static/common/js/wgen/threetwelve/Ajax.js')

    request2062.GET('/outcomes/static/js/overlay/ItemAnalysisOverlay.js')

    grinder.sleep(55)
    request2063.GET('/outcomes/static/js/overlay/ItemAnalysisData.js')

    request2064.GET('/outcomes/static/js/overlay/StandardAnalysisOverlay.js')

    grinder.sleep(49)
    request2065.GET('/outcomes/static/js/overlay/StandardAnalysisData.js')

    request2066.GET('/outcomes/static/js/matrix/MatrixUI.js')

    request2067.GET('/outcomes/static/js/matrix/MatrixData.js')

    request2068.GET('/outcomes/static/js/learningMap/LearningMapUI.js')

    grinder.sleep(48)
    request2069.GET('/outcomes/static/js/learningMap/LearningMapData.js')

    request2070.GET('/outcomes/static/js/ReportsUI.js')

    grinder.sleep(47)
    request2071.GET('/outcomes/static/js/ReportsPage.js')

    request2072.GET('/outcomes/static/js/reports_ready.js')

    request2073.GET('/outcomes/static/js/widgets/InstHierarchyDropdownPicker.js')

    grinder.sleep(29)
    request2074.GET('/outcomes/static/common/js/widgets/GlobalNavBar.js')

    return result

  def page21(self):
    """GET staff (request 2101)."""
    self.token_inst_id = \
      '159'
    self.token__ = \
      '1293560264487'
    result = request2101.GET('/outcomes/webservices/inst/staff' +
      '?inst_id=' +
      self.token_inst_id +
      '&_=' +
      self.token__)

    return result

  def page22(self):
    """GET classes (request 2201)."""
    self.token__ = \
      '1293560264497'
    result = request2201.GET('/outcomes/webservices/inst/classes' +
      '?inst_id=' +
      self.token_inst_id +
      '&_=' +
      self.token__)

    return result

  def page23(self):
    """GET assessments (request 2301)."""
    self.token_classeId = \
      '5'
    self.token_subjectCode = \
      'ELA'
    self.token__ = \
      '1293560264623'
    result = request2301.GET('/outcomes/classe/assessments' +
      '?classeId=' +
      self.token_classeId +
      '&subjectCode=' +
      self.token_subjectCode +
      '&_=' +
      self.token__)

    return result

  def page24(self):
    """GET studentList (requests 2401-2402)."""
    self.token_assessmentId = \
      '15'
    self.token__ = \
      '1293560267950'
    result = request2401.GET('/outcomes/map/studentList' +
      '?assessmentId=' +
      self.token_assessmentId +
      '&classeId=' +
      self.token_classeId +
      '&_=' +
      self.token__)

    request2402.GET('/outcomes/static/images/ajax-loader-lrg.gif')

    return result

  def page25(self):
    """GET classeMap (requests 2501-2506)."""
    self.token_hexMapWidth = \
      '700'
    self.token_hexMapHeight = \
      '1324'
    self.token__ = \
      '1293560267971'
    result = request2501.GET('/outcomes/map/classeMap' +
      '?assessmentId=' +
      self.token_assessmentId +
      '&classeId=' +
      self.token_classeId +
      '&hexMapWidth=' +
      self.token_hexMapWidth +
      '&hexMapHeight=' +
      self.token_hexMapHeight +
      '&_=' +
      self.token__)

    grinder.sleep(60)
    request2502.GET('/outcomes/static/images/matrix/legend/click_to_open.png')

    request2503.GET('/outcomes/static/images/matrix/legend/click_to_close.png')

    request2504.GET('/outcomes/static/images/learningMap/student_list_header.png')

    request2505.GET('/outcomes/static/images/learningMap/icon_student_not_faded.png')

    request2506.GET('/outcomes/static/images/learningMap/cells.png')

    return result

  def page26(self):
    """GET ellipsis.xml (requests 2601-2606)."""
    result = request2601.GET('/outcomes/static/css/ellipsis.xml')

    request2602.GET('/outcomes/static/images/learningMap/question_mark_cell.png')

    request2603.GET('/outcomes/static/images/learningMap/legend/legend_tab.png')

    grinder.sleep(35)
    request2604.GET('/outcomes/static/js/hexmap/assets/clear.gif')

    request2605.GET('/outcomes/static/js/hexmap/assets/ui_tile_dark.png')

    request2606.GET('/outcomes/static/js/hexmap/assets/ui_sprite.png')

    return result

  def page27(self):
    """GET info (requests 2701-2703)."""
    self.token_map_id = \
      'symbols_assmt15_class5'
    self.token__ = \
      '1293560268629'
    result = request2701.GET('/outcomes/map/info' +
      '?map_id=' +
      self.token_map_id +
      '&_=' +
      self.token__)

    request2702.GET('/outcomes/static/js/hexmap/assets/ui_grid_tile.png')

    request2703.GET('/outcomes/static/js/hexmap/assets/ui_pan.png')

    return result

  def page28(self):
    """GET tile (request 2801)."""
    self.token_tile_id = \
      '115'
    result = request2801.GET('/outcomes/map/tile' +
      '?tile_id=' +
      self.token_tile_id)

    return result

  def page29(self):
    """GET tile (request 2901)."""
    self.token_tile_id = \
      '116'
    result = request2901.GET('/outcomes/map/tile' +
      '?tile_id=' +
      self.token_tile_id)

    return result

  def page30(self):
    """GET tile (request 3001)."""
    self.token_tile_id = \
      '117'
    result = request3001.GET('/outcomes/map/tile' +
      '?tile_id=' +
      self.token_tile_id)

    return result

  def page31(self):
    """GET ChFnb29nLXBoaXNoLXNoYXZhchABGIGIBCCAnAQqwgIVBAEA______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________8PMgcBBAEA__8P (request 3101)."""
    result = request3101.GET('/safebrowsing/rd/ChFnb29nLXBoaXNoLXNoYXZhchABGIGIBCCAnAQqwgIVBAEA______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________8PMgcBBAEA__8P')

    return result

  def page32(self):
    """GET ChFnb29nLXBoaXNoLXNoYXZhchAAGIHjByCA6AcyVYHxAQD___________________v_9ff________f7__9_____89_ev__df_______3_uuf7_93v_8773__-isv_______2-1tfPjf3in3r38X9n-_wA (request 3201)."""
    result = request3201.GET('/safebrowsing/rd/ChFnb29nLXBoaXNoLXNoYXZhchAAGIHjByCA6AcyVYHxAQD___________________v_9ff________f7__9_____89_ev__df_______3_uuf7_93v_8773__-isv_______2-1tfPjf3in3r38X9n-_wA')

    return result

  def page33(self):
    """GET ChFnb29nLXBoaXNoLXNoYXZhchAAGIHoByDA6gcyLQH0AQD____f___vf_X__________f____________v___3___v_________AA (request 3301)."""
    result = request3301.GET('/safebrowsing/rd/ChFnb29nLXBoaXNoLXNoYXZhchAAGIHoByDA6gcyLQH0AQD____f___vf_X__________f____________v___3___v_________AA')

    return result

  def page34(self):
    """GET ChFnb29nLXBoaXNoLXNoYXZhchAAGMHqByCA7QcyLEL1AQD_______________________________________f___________9_ (request 3401)."""
    result = request3401.GET('/safebrowsing/rd/ChFnb29nLXBoaXNoLXNoYXZhchAAGMHqByCA7QcyLEL1AQD_______________________________________f___________9_')

    return result

  def page35(self):
    """GET ChFnb29nLXBoaXNoLXNoYXZhchAAGIHtByDA7wcyLYH2AQD_____________________________________________________AA (request 3501)."""
    result = request3501.GET('/safebrowsing/rd/ChFnb29nLXBoaXNoLXNoYXZhchAAGIHtByDA7wcyLYH2AQD_____________________________________________________AA')

    return result

  def page36(self):
    """GET ChFnb29nLXBoaXNoLXNoYXZhchAAGMHvByCA8gcqHEL4AQD______________________________38yFcH3AQD_____________________AQ (request 3601)."""
    result = request3601.GET('/safebrowsing/rd/ChFnb29nLXBoaXNoLXNoYXZhchAAGMHvByCA8gcqHEL4AQD______________________________38yFcH3AQD_____________________AQ')

    return result

  def page37(self):
    """GET home (request 3701)."""
    result = request3701.GET('/oib/home')

    return result

  def page38(self):
    """GET recent (request 3801)."""
    self.token__ = \
      '1293560304391'
    result = request3801.GET('/oib/webservices/entities/recent' +
      '?type=' +
      self.token_type +
      '&pageSize=' +
      self.token_pageSize +
      '&page=' +
      self.token_page +
      '&_=' +
      self.token__)

    return result

  def page39(self):
    """POST base (requests 3901-3910)."""
    result = request3901.POST('/oib/assessment/view/base',
      ( NVPair('id', '342'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    grinder.sleep(228)
    self.token__ = \
      '1293560320375'
    request3902.GET('/oib/static/common/js/wgen/threetwelve/Ajax.js' +
      '?_=' +
      self.token__)

    grinder.sleep(33)
    self.token__ = \
      '1293560320418'
    request3903.GET('/oib/static/common/js/widgets/Button.js' +
      '?_=' +
      self.token__)

    grinder.sleep(81)
    self.token__ = \
      '1293560320496'
    request3904.GET('/oib/static/common/js/3p/jqueryMultiSelect.js' +
      '?_=' +
      self.token__)

    grinder.sleep(910)
    self.token__ = \
      '1293560321425'
    request3905.GET('/oib/static/js/widgets/PopulationHierarchyBrowser.js' +
      '?_=' +
      self.token__)

    grinder.sleep(12)
    self.token__ = \
      '1293560321442'
    request3906.GET('/oib/static/js/widgets/PopulationHierarchyBrowserData.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1293560321459'
    request3907.GET('/oib/static/js/widgets/PopulationHierarchyBrowserUI.js' +
      '?_=' +
      self.token__)

    grinder.sleep(47)
    self.token__ = \
      '1293560321516'
    request3908.GET('/oib/static/js/widgets/AssignmentCreator.js' +
      '?_=' +
      self.token__)

    grinder.sleep(45)
    self.token__ = \
      '1293560321570'
    request3909.GET('/oib/static/js/widgets/AssignmentViewer.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1293560321583'
    request3910.GET('/oib/static/js/assignment/MyAssignmentsPage.js' +
      '?_=' +
      self.token__)

    return result

  def page40(self):
    """GET list (request 4001)."""
    self.token_assessmentId = \
      '31'
    self.token__ = \
      '1293560321600'
    result = request4001.GET('/oib/assignment/list' +
      '?assessmentId=' +
      self.token_assessmentId +
      '&_=' +
      self.token__)

    return result

  def page41(self):
    """GET create (requests 4101-4103)."""
    self.token__ = \
      '1293560321602'
    result = request4101.GET('/oib/assignment/create' +
      '?_=' +
      self.token__ +
      '&assessmentId=' +
      self.token_assessmentId)

    self.token__ = \
      '1293560321604'
    request4102.GET('/oib/static/js/widgets/sharing.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1293560321764'
    request4103.GET('/oib/static/js/widgets/SharingDropdown.js' +
      '?_=' +
      self.token__)

    return result

  def page42(self):
    """POST base (requests 4201-4210)."""
    result = request4201.POST('/oib/assessment/view/base',
      ( NVPair('id', '1393'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    grinder.sleep(349)
    self.token__ = \
      '1293560326139'
    request4202.GET('/oib/static/common/js/wgen/threetwelve/Ajax.js' +
      '?_=' +
      self.token__)

    grinder.sleep(378)
    self.token__ = \
      '1293560326836'
    request4203.GET('/oib/static/common/js/widgets/Button.js' +
      '?_=' +
      self.token__)

    grinder.sleep(18)
    self.token__ = \
      '1293560326862'
    request4204.GET('/oib/static/common/js/3p/jqueryMultiSelect.js' +
      '?_=' +
      self.token__)

    grinder.sleep(47)
    self.token__ = \
      '1293560326917'
    request4205.GET('/oib/static/js/widgets/PopulationHierarchyBrowser.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1293560326929'
    request4206.GET('/oib/static/js/widgets/PopulationHierarchyBrowserData.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1293560326942'
    request4207.GET('/oib/static/js/widgets/PopulationHierarchyBrowserUI.js' +
      '?_=' +
      self.token__)

    grinder.sleep(46)
    self.token__ = \
      '1293560326998'
    request4208.GET('/oib/static/js/widgets/AssignmentCreator.js' +
      '?_=' +
      self.token__)

    grinder.sleep(45)
    self.token__ = \
      '1293560327052'
    request4209.GET('/oib/static/js/widgets/AssignmentViewer.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1293560327065'
    request4210.GET('/oib/static/js/assignment/MyAssignmentsPage.js' +
      '?_=' +
      self.token__)

    return result

  def page43(self):
    """GET list (request 4301)."""
    self.token_assessmentId = \
      '74'
    self.token__ = \
      '1293560327088'
    result = request4301.GET('/oib/assignment/list' +
      '?assessmentId=' +
      self.token_assessmentId +
      '&_=' +
      self.token__)

    return result

  def page44(self):
    """GET create (requests 4401-4403)."""
    self.token__ = \
      '1293560327090'
    result = request4401.GET('/oib/assignment/create' +
      '?_=' +
      self.token__ +
      '&assessmentId=' +
      self.token_assessmentId)

    self.token__ = \
      '1293560327091'
    request4402.GET('/oib/static/js/widgets/sharing.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1293560327251'
    request4403.GET('/oib/static/js/widgets/SharingDropdown.js' +
      '?_=' +
      self.token__)

    return result

  def page45(self):
    """GET create (requests 4501-4521)."""
    self.token_fromManage = \
      'false'
    result = request4501.GET('/oib/item/create' +
      '?fromManage=' +
      self.token_fromManage)

    grinder.sleep(110)
    request4502.GET('/oib/static/css/create/create.css')

    grinder.sleep(22)
    request4503.GET('/oib/static/images/icon_view_detail.png')

    request4504.GET('/oib/static/images/sprites/slider_sprite.png')

    grinder.sleep(41)
    request4505.GET('/oib/static/images/manage/locate_tab_arrows.png')

    grinder.sleep(377)
    request4506.GET('/oib/static/css//widgets/CollapsibleBox.css')

    request4507.GET('/oib/static/images/connectors/create_box_bottom_connector.png')

    request4508.GET('/oib/static/css/create/create_item.css')

    request4509.GET('/oib/static/images/mc_delete.png')

    request4510.GET('/oib/static/images/connectors/create_box_top_connector.png')

    grinder.sleep(230)
    request4511.GET('/oib/static/js//widgets/CollapsibleBox.js')

    grinder.sleep(40)
    request4512.GET('/oib/static/js/widgets/collapsible_panel.js')

    grinder.sleep(29)
    request4513.GET('/oib/static/js/widgets/sliders/GradeRangeSlider.js')

    request4514.GET('/oib/static/js/widgets/sliders/TimeSlider.js')

    grinder.sleep(16)
    request4515.GET('/oib/static/js/AlignableItemBankEntity.js')

    grinder.sleep(17)
    request4516.GET('/oib/static/js/item/Item.js')

    grinder.sleep(19)
    request4517.GET('/oib/static/js/item/LinkedPassage.js')

    grinder.sleep(12)
    request4518.GET('/oib/static/js/item/LinkedRubrics.js')

    request4519.GET('/oib/static/js/item/OpenResponseScoring.js')

    request4520.GET('/oib/static/js/EditReady.js')

    grinder.sleep(164)
    request4521.GET('/oib/static/images/sprites/standards_puffy_cookie_crumb.png')

    return result

  def page46(self):
    """GET standardsTree (request 4601)."""
    self.token__ = \
      '1293560346510'
    self.token_subject = \
      'ELA'
    self.token_rootId = \
      '33807'
    self.token_echo = \
      '0'
    result = request4601.GET('/oib/standards/generic/standardsTree' +
      '?_=' +
      self.token__ +
      '&subject=' +
      self.token_subject +
      '&rootId=' +
      self.token_rootId +
      '&echo=' +
      self.token_echo)

    return result

  def page47(self):
    """GET standardsTree (request 4701)."""
    self.token__ = \
      '1293560346522'
    self.token_rootId = \
      '42985'
    self.token_echo = \
      '1'
    result = request4701.GET('/oib/standards/generic/standardsTree' +
      '?_=' +
      self.token__ +
      '&subject=' +
      self.token_subject +
      '&rootId=' +
      self.token_rootId +
      '&echo=' +
      self.token_echo)

    return result

  def page48(self):
    """GET standardsTree (request 4801)."""
    self.token__ = \
      '1293560346532'
    self.token_rootId = \
      '51605'
    self.token_echo = \
      '2'
    result = request4801.GET('/oib/standards/generic/standardsTree' +
      '?_=' +
      self.token__ +
      '&subject=' +
      self.token_subject +
      '&rootId=' +
      self.token_rootId +
      '&echo=' +
      self.token_echo)

    return result

  def page49(self):
    """GET standardsTree (request 4901)."""
    self.token__ = \
      '1293560346541'
    self.token_rootId = \
      '4951'
    self.token_echo = \
      '3'
    result = request4901.GET('/oib/standards/generic/standardsTree' +
      '?_=' +
      self.token__ +
      '&subject=' +
      self.token_subject +
      '&rootId=' +
      self.token_rootId +
      '&echo=' +
      self.token_echo)

    return result

  def page50(self):
    """GET standardsTree (request 5001)."""
    self.token__ = \
      '1293560346550'
    self.token_rootId = \
      '43133'
    self.token_echo = \
      '4'
    result = request5001.GET('/oib/standards/generic/standardsTree' +
      '?_=' +
      self.token__ +
      '&subject=' +
      self.token_subject +
      '&rootId=' +
      self.token_rootId +
      '&echo=' +
      self.token_echo)

    return result

  def page51(self):
    """GET standardsTree (requests 5101-5104)."""
    self.token__ = \
      '1293560346562'
    self.token_rootId = \
      '43887'
    self.token_echo = \
      '5'
    result = request5101.GET('/oib/standards/generic/standardsTree' +
      '?_=' +
      self.token__ +
      '&subject=' +
      self.token_subject +
      '&rootId=' +
      self.token_rootId +
      '&echo=' +
      self.token_echo)

    request5102.GET('/oib/static/images/slider.png')

    request5103.GET('/oib/static/images/create/btn_section_expander_item.png')

    request5104.GET('/oib/static/images/create/btn_section_expander_item_closed.png')

    return result

  def page52(self):
    """GET standardsTreeGrandkids (request 5201)."""
    self.token__ = \
      '1293560348666'
    self.token_nodeId = \
      '34027'
    self.token_echo = \
      '0'
    result = request5201.GET('/oib/standards/generic/standardsTreeGrandkids' +
      '?_=' +
      self.token__ +
      '&nodeId=' +
      self.token_nodeId +
      '&echo=' +
      self.token_echo)

    return result

  def page53(self):
    """GET standardsTreeGrandkids (requests 5301-5334)."""
    self.token__ = \
      '1293560349200'
    self.token_nodeId = \
      '34059'
    result = request5301.GET('/oib/standards/generic/standardsTreeGrandkids' +
      '?_=' +
      self.token__ +
      '&nodeId=' +
      self.token_nodeId +
      '&echo=' +
      self.token_echo)

    grinder.sleep(407)
    request5302.GET('/oib/static/images/icon_caret_blue_down.png')

    request5303.GET('/oib/static/images/btn_radio.png')

    grinder.sleep(2976)
    request5304.GET('/oib/static/images/multipleChoice/mc_box_inner_top.gif')

    request5305.GET('/oib/static/images/multipleChoice/arranger/mc_arranger_buttons.png')

    grinder.sleep(336)
    request5306.GET('/oib/static/images/multipleChoice/mc_box_inner_bottom.gif')

    grinder.sleep(1982)
    request5307.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/langs/en.js')

    request5308.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/editor_template.js')

    request5309.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/table/editor_plugin.js')

    grinder.sleep(20)
    request5310.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/editor_plugin.js')

    request5311.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelveimage/editor_plugin.js')

    request5312.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/editor_plugin.js')

    request5313.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/advimagescale/editor_plugin.js')

    request5314.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/editor_plugin.js')

    request5315.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/atomic/editor_plugin.js')

    grinder.sleep(45)
    request5316.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/langs/en.js')

    grinder.sleep(81)
    request5317.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/paste/editor_plugin.js')

    request5318.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/inlinepopups/editor_plugin.js')

    request5319.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/autoresize/editor_plugin.js')

    grinder.sleep(110)
    request5320.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui.css')

    request5321.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui_threetwelve.css')

    request5322.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/inlinepopups/skins/clearlooks2/window.css')

    grinder.sleep(114)
    request5323.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/content.css')

    grinder.sleep(21)
    request5324.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/img/icons.gif')

    request5325.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/img/button_bg.png')

    grinder.sleep(14)
    request5326.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/img/small.png')

    request5327.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/img/medium.png')

    grinder.sleep(15)
    request5328.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_add_space_unruled.png')

    request5329.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/img/large.png')

    request5330.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/img/ed_mathformula.gif')

    request5331.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_space_title_1.gif')

    request5332.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_space_title_2.gif')

    request5333.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_space_title_3.gif')

    request5334.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_add_space_ruled.png')

    return result

  def page54(self):
    """GET manage (requests 5401-5425)."""
    self.token__ = \
      '1293560360084'
    self.token_forSelect = \
      'true'
    result = request5401.GET('/oib/rubric/manage' +
      '?_=' +
      self.token__ +
      '&subject=' +
      self.token_subject +
      '&forSelect=' +
      self.token_forSelect)

    grinder.sleep(173)
    request5402.GET('/oib/static/images/manage/search/red_cancel_icon.png')

    grinder.sleep(1357)
    request5403.GET('/oib/static/images/manage/left_pane_background.png')

    grinder.sleep(1201)
    request5404.GET('/oib/static/images/manage/search/search_within_bttn.png')

    grinder.sleep(208)
    self.token__ = \
      '1293560362978'
    request5405.GET('/oib/static/js/ViewItemBankEntity.js' +
      '?_=' +
      self.token__)

    grinder.sleep(271)
    request5406.GET('/oib/static/images/manage/search/search_within_glass.png')

    grinder.sleep(228)
    self.token__ = \
      '1293560366126'
    request5407.GET('/oib/static/js/widgets/sharing.js' +
      '?_=' +
      self.token__)

    request5408.GET('/oib/static/images/manage/locate_stroke_quantity_results_bg.png')

    grinder.sleep(73)
    self.token__ = \
      '1293560366352'
    request5409.GET('/oib/static/js/standardsBrowser/createStandardsUi.js' +
      '?_=' +
      self.token__)

    grinder.sleep(77)
    self.token__ = \
      '1293560366439'
    request5410.GET('/oib/static/js/standardsBrowser/viewStandardsUi.js' +
      '?_=' +
      self.token__)

    grinder.sleep(80)
    self.token__ = \
      '1293560366522'
    request5411.GET('/oib/static/js/widgets/tooltip.js' +
      '?_=' +
      self.token__)

    grinder.sleep(70)
    self.token__ = \
      '1293560366602'
    request5412.GET('/oib/static/js/widgets/AssignmentCreator.js' +
      '?_=' +
      self.token__)

    grinder.sleep(76)
    self.token__ = \
      '1293560366687'
    request5413.GET('/oib/static/js/EntityPopupSourceUI.js' +
      '?_=' +
      self.token__)

    grinder.sleep(69)
    self.token__ = \
      '1293560366764'
    request5414.GET('/oib/static/js/manage/ManageBrowser.js' +
      '?_=' +
      self.token__)

    grinder.sleep(91)
    self.token__ = \
      '1293560366870'
    request5415.GET('/oib/static/js/manage/ManageBrowserRenderer.js' +
      '?_=' +
      self.token__)

    grinder.sleep(68)
    self.token__ = \
      '1293560366946'
    request5416.GET('/oib/static/js/manage/ManageRubricBrowserRenderer.js' +
      '?_=' +
      self.token__)

    grinder.sleep(76)
    self.token__ = \
      '1293560367029'
    request5417.GET('/oib/static/js/standardsBrowser/ManageStandardsUi.js' +
      '?_=' +
      self.token__)

    grinder.sleep(81)
    self.token__ = \
      '1293560367115'
    request5418.GET('/oib/static/js/manage/AssessmentFilterWidget.js' +
      '?_=' +
      self.token__)

    grinder.sleep(73)
    self.token__ = \
      '1293560367200'
    request5419.GET('/oib/static/js/manage/ManageFilterWidget.js' +
      '?_=' +
      self.token__)

    grinder.sleep(71)
    self.token__ = \
      '1293560367280'
    request5420.GET('/oib/static/js/item/question/QuestionType.js' +
      '?_=' +
      self.token__)

    grinder.sleep(69)
    self.token__ = \
      '1293560367358'
    request5421.GET('/oib/static/js/item/question/OpenResponseQuestionType.js' +
      '?_=' +
      self.token__)

    grinder.sleep(73)
    self.token__ = \
      '1293560367444'
    request5422.GET('/oib/static/js/widgets/SubjectDropdown.js' +
      '?_=' +
      self.token__)

    grinder.sleep(74)
    self.token__ = \
      '1293560367527'
    request5423.GET('/oib/static/js/widgets/EditPageSubjectDropdown.js' +
      '?_=' +
      self.token__)

    grinder.sleep(73)
    self.token__ = \
      '1293560367606'
    request5424.GET('/oib/static/common/js/3p/jqueryMultiSelect.js' +
      '?_=' +
      self.token__)

    grinder.sleep(148)
    self.token__ = \
      '1293560367768'
    request5425.GET('/oib/static/js/manage/manage_ready.js' +
      '?_=' +
      self.token__)

    return result

  def page55(self):
    """GET myStandardsRootNodes (request 5501)."""
    self.token__ = \
      '1293560367941'
    self.token_getAlignCount = \
      'true'
    result = request5501.GET('/oib/standards/rubric/myStandardsRootNodes' +
      '?_=' +
      self.token__ +
      '&echo=' +
      self.token_echo +
      '&getAlignCount=' +
      self.token_getAlignCount +
      '&subject=' +
      self.token_subject)

    return result

  def page56(self):
    """GET getAll (requests 5601-5602)."""
    self.token__ = \
      '1293560367944'
    self.token_sort = \
      'title'
    self.token_sortDir = \
      'asc'
    self.token_searchString = \
      ''
    self.token_filterString = \
      '{}'
    result = request5601.GET('/oib/rubric/manage/getAll' +
      '?_=' +
      self.token__ +
      '&sort=' +
      self.token_sort +
      '&sortDir=' +
      self.token_sortDir +
      '&subject=' +
      self.token_subject +
      '&page=' +
      self.token_page +
      '&forSelect=' +
      self.token_forSelect +
      '&searchString=' +
      self.token_searchString +
      '&filterString=' +
      self.token_filterString)

    grinder.sleep(39)
    request5602.GET('/oib/static/images/manage/standards_bullet_image.png')

    return result

  def page57(self):
    """GET renderRubricOverview (request 5701)."""
    self.token__ = \
      '1293560379765'
    self.token_id = \
      '673'
    self.token_version = \
      '1'
    result = request5701.GET('/oib/renderRubricOverview' +
      '?_=' +
      self.token__ +
      '&id=' +
      self.token_id +
      '&version=' +
      self.token_version)

    return result

  def page58(self):
    """POST items (request 5801)."""
    result = request5801.POST('/oib/pools/list/items',
      ( NVPair('itemJSON', '{\"subjectCode\": \"ELA\", \"title\": \"test\", \"estTimeSecs\": null, \"body\": {\"item_type\": \"OR\", \"main_content\": \"<p>sdfafafsdfsdff</p>\", \"append_pages\": {\"type\": \"\", \"size\": \"0\"}}, \"alignGrade\": {}, \"rubricVCIDs\": [673], \"rubricVersionNums\": [1]}'),
        NVPair('poolId', '463'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page59(self):
    """POST sharingAgreement (request 5901)."""
    result = request5901.POST('/oib/sharingAgreement',
      '',
      ( NVPair('Content-Type', 'application/xml; charset=UTF-8'), ))

    return result

  def page60(self):
    """POST saveDraft (request 6001)."""
    result = request6001.POST('/oib/saveDraft',
      ( NVPair('itemJSON', '{\"subjectCode\": \"ELA\", \"title\": \"test\", \"estTimeSecs\": null, \"body\": {\"item_type\": \"OR\", \"main_content\": \"<p>sdfafafsdfsdff</p>\", \"append_pages\": {\"type\": \"\", \"size\": \"0\"}}, \"alignGrade\": {}, \"rubricVCIDs\": [673], \"rubricVersionNums\": [1]}'),
        NVPair('alignmentJSON', '{\"alignStandards\": [34075]}'),
        NVPair('poolId', '463'),
        NVPair('ctoken', 'woadIOum'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def __call__(self):
    """This method is called for every run performed by the worker thread."""
    self.page1()      # GET login (requests 101-181)

    grinder.sleep(36)
    self.page2()      # GET recent (requests 201-202)

    grinder.sleep(16)
    self.page3()      # GET ellipsis.xml (requests 301-306)

    grinder.sleep(293)
    self.page4()      # POST base (requests 401-415)

    grinder.sleep(13)
    self.page5()      # GET list (request 501)
    self.page6()      # GET create (requests 601-611)

    grinder.sleep(2068)
    self.page7()      # GET clone (request 701)

    grinder.sleep(11251)
    self.page8()      # POST sharingAgreement (request 801)

    grinder.sleep(52715)
    self.page9()      # GET keepalive (request 901)

    grinder.sleep(910089)
    self.page10()     # POST downloads (request 1001)

    grinder.sleep(61)
    self.page11()     # GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAEY79QCIPjUAioGcKoAAP8BMgVvqgAAAQ (request 1101)

    grinder.sleep(47)
    self.page12()     # GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYodgBIMDZATIZIWwAAP____-__7f7v_____3____f__7_AA (request 1201)

    grinder.sleep(85226)
    self.page13()     # GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYwegBIIDrATItQXQAAP_v_______v_9______7______vv___9____9_v7_7_9__-_9____cA (request 1301)

    grinder.sleep(1016)
    self.page14()     # GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYgesBIMDtATItgXUAAP3__-_____9___v______-______________3___________v6__78A (request 1401)

    grinder.sleep(696)
    self.page15()     # GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYwe0BIIDwATItwXYAAP____v___d_3____vf7_f_____7__________________________8A (request 1501)

    grinder.sleep(826)
    self.page16()     # GET ChNnb29nLW1hbHdhcmUtc2hhdmFyEAAYgfABIICEAiqoAuR4AAD___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________8fMiEBeAAA_7_ff_9______________________________wc (request 1601)

    grinder.sleep(482)
    self.page17()     # GET ChFnb29nLXBoaXNoLXNoYXZhchABGLGCBCCAgwQyDzEBAQD_____-_______AA (request 1701)

    grinder.sleep(1555)
    self.page18()     # GET ChFnb29nLXBoaXNoLXNoYXZhchABGIGDBCCAiAQyVYEBAQD___9________________________________3_____________________________________________________________________wA (request 1801)

    grinder.sleep(48622)
    self.page19()     # POST save (request 1901)

    grinder.sleep(5370)
    self.page20()     # GET view (requests 2001-2074)

    grinder.sleep(96)
    self.page21()     # GET staff (request 2101)
    self.page22()     # GET classes (request 2201)

    grinder.sleep(56)
    self.page23()     # GET assessments (request 2301)

    grinder.sleep(3205)
    self.page24()     # GET studentList (requests 2401-2402)
    self.page25()     # GET classeMap (requests 2501-2506)
    self.page26()     # GET ellipsis.xml (requests 2601-2606)

    grinder.sleep(12)
    self.page27()     # GET info (requests 2701-2703)

    grinder.sleep(45)
    self.page28()     # GET tile (request 2801)
    self.page29()     # GET tile (request 2901)
    self.page30()     # GET tile (request 3001)

    grinder.sleep(1285)
    self.page31()     # GET ChFnb29nLXBoaXNoLXNoYXZhchABGIGIBCCAnAQqwgIVBAEA______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________8PMgcBBAEA__8P (request 3101)

    grinder.sleep(65)
    self.page32()     # GET ChFnb29nLXBoaXNoLXNoYXZhchAAGIHjByCA6AcyVYHxAQD___________________v_9ff________f7__9_____89_ev__df_______3_uuf7_93v_8773__-isv_______2-1tfPjf3in3r38X9n-_wA (request 3201)

    grinder.sleep(780)
    self.page33()     # GET ChFnb29nLXBoaXNoLXNoYXZhchAAGIHoByDA6gcyLQH0AQD____f___vf_X__________f____________v___3___v_________AA (request 3301)

    grinder.sleep(725)
    self.page34()     # GET ChFnb29nLXBoaXNoLXNoYXZhchAAGMHqByCA7QcyLEL1AQD_______________________________________f___________9_ (request 3401)

    grinder.sleep(853)
    self.page35()     # GET ChFnb29nLXBoaXNoLXNoYXZhchAAGIHtByDA7wcyLYH2AQD_____________________________________________________AA (request 3501)

    grinder.sleep(1791)
    self.page36()     # GET ChFnb29nLXBoaXNoLXNoYXZhchAAGMHvByCA8gcqHEL4AQD______________________________38yFcH3AQD_____________________AQ (request 3601)

    grinder.sleep(28860)
    self.page37()     # GET home (request 3701)

    grinder.sleep(495)
    self.page38()     # GET recent (request 3801)

    grinder.sleep(13445)
    self.page39()     # POST base (requests 3901-3910)

    grinder.sleep(34)
    self.page40()     # GET list (request 4001)
    self.page41()     # GET create (requests 4101-4103)

    grinder.sleep(997)
    self.page42()     # POST base (requests 4201-4210)

    grinder.sleep(40)
    self.page43()     # GET list (request 4301)
    self.page44()     # GET create (requests 4401-4403)

    grinder.sleep(17500)
    self.page45()     # GET create (requests 4501-4521)
    self.page46()     # GET standardsTree (request 4601)
    self.page47()     # GET standardsTree (request 4701)
    self.page48()     # GET standardsTree (request 4801)
    self.page49()     # GET standardsTree (request 4901)
    self.page50()     # GET standardsTree (request 5001)
    self.page51()     # GET standardsTree (requests 5101-5104)

    grinder.sleep(1134)
    self.page52()     # GET standardsTreeGrandkids (request 5201)

    grinder.sleep(513)
    self.page53()     # GET standardsTreeGrandkids (requests 5301-5334)

    grinder.sleep(6989)
    self.page54()     # GET manage (requests 5401-5425)

    grinder.sleep(198)
    self.page55()     # GET myStandardsRootNodes (request 5501)
    self.page56()     # GET getAll (requests 5601-5602)

    grinder.sleep(2156)
    self.page57()     # GET renderRubricOverview (request 5701)

    grinder.sleep(82)
    self.page58()     # POST items (request 5801)

    grinder.sleep(1420)
    self.page59()     # POST sharingAgreement (request 5901)

    grinder.sleep(1620)
    self.page60()     # POST saveDraft (request 6001)


def instrumentMethod(test, method_name, c=TestRunner):
  """Instrument a method with the given Test."""
  unadorned = getattr(c, method_name)
  import new
  method = new.instancemethod(test.wrap(unadorned), None, c)
  setattr(c, method_name, method)

# Replace each method with an instrumented version.
# You can call the unadorned method using self.page1.__target__().
instrumentMethod(Test(100, 'Page 1'), 'page1')
instrumentMethod(Test(200, 'Page 2'), 'page2')
instrumentMethod(Test(300, 'Page 3'), 'page3')
instrumentMethod(Test(400, 'Page 4'), 'page4')
instrumentMethod(Test(500, 'Page 5'), 'page5')
instrumentMethod(Test(600, 'Page 6'), 'page6')
instrumentMethod(Test(700, 'Page 7'), 'page7')
instrumentMethod(Test(800, 'Page 8'), 'page8')
instrumentMethod(Test(900, 'Page 9'), 'page9')
instrumentMethod(Test(1000, 'Page 10'), 'page10')
instrumentMethod(Test(1100, 'Page 11'), 'page11')
instrumentMethod(Test(1200, 'Page 12'), 'page12')
instrumentMethod(Test(1300, 'Page 13'), 'page13')
instrumentMethod(Test(1400, 'Page 14'), 'page14')
instrumentMethod(Test(1500, 'Page 15'), 'page15')
instrumentMethod(Test(1600, 'Page 16'), 'page16')
instrumentMethod(Test(1700, 'Page 17'), 'page17')
instrumentMethod(Test(1800, 'Page 18'), 'page18')
instrumentMethod(Test(1900, 'Page 19'), 'page19')
instrumentMethod(Test(2000, 'Page 20'), 'page20')
instrumentMethod(Test(2100, 'Page 21'), 'page21')
instrumentMethod(Test(2200, 'Page 22'), 'page22')
instrumentMethod(Test(2300, 'Page 23'), 'page23')
instrumentMethod(Test(2400, 'Page 24'), 'page24')
instrumentMethod(Test(2500, 'Page 25'), 'page25')
instrumentMethod(Test(2600, 'Page 26'), 'page26')
instrumentMethod(Test(2700, 'Page 27'), 'page27')
instrumentMethod(Test(2800, 'Page 28'), 'page28')
instrumentMethod(Test(2900, 'Page 29'), 'page29')
instrumentMethod(Test(3000, 'Page 30'), 'page30')
instrumentMethod(Test(3100, 'Page 31'), 'page31')
instrumentMethod(Test(3200, 'Page 32'), 'page32')
instrumentMethod(Test(3300, 'Page 33'), 'page33')
instrumentMethod(Test(3400, 'Page 34'), 'page34')
instrumentMethod(Test(3500, 'Page 35'), 'page35')
instrumentMethod(Test(3600, 'Page 36'), 'page36')
instrumentMethod(Test(3700, 'Page 37'), 'page37')
instrumentMethod(Test(3800, 'Page 38'), 'page38')
instrumentMethod(Test(3900, 'Page 39'), 'page39')
instrumentMethod(Test(4000, 'Page 40'), 'page40')
instrumentMethod(Test(4100, 'Page 41'), 'page41')
instrumentMethod(Test(4200, 'Page 42'), 'page42')
instrumentMethod(Test(4300, 'Page 43'), 'page43')
instrumentMethod(Test(4400, 'Page 44'), 'page44')
instrumentMethod(Test(4500, 'Page 45'), 'page45')
instrumentMethod(Test(4600, 'Page 46'), 'page46')
instrumentMethod(Test(4700, 'Page 47'), 'page47')
instrumentMethod(Test(4800, 'Page 48'), 'page48')
instrumentMethod(Test(4900, 'Page 49'), 'page49')
instrumentMethod(Test(5000, 'Page 50'), 'page50')
instrumentMethod(Test(5100, 'Page 51'), 'page51')
instrumentMethod(Test(5200, 'Page 52'), 'page52')
instrumentMethod(Test(5300, 'Page 53'), 'page53')
instrumentMethod(Test(5400, 'Page 54'), 'page54')
instrumentMethod(Test(5500, 'Page 55'), 'page55')
instrumentMethod(Test(5600, 'Page 56'), 'page56')
instrumentMethod(Test(5700, 'Page 57'), 'page57')
instrumentMethod(Test(5800, 'Page 58'), 'page58')
instrumentMethod(Test(5900, 'Page 59'), 'page59')
instrumentMethod(Test(6000, 'Page 60'), 'page60')
