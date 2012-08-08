# The Grinder 3.4
# HTTP script recorded by TCPProxy at Jan 24, 2011 12:18:48 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
from com.xhaus.jyson import JysonCodec as json

connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Language', 'en-us,en;q=0.5'),
    NVPair('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),
    # NVPair('Accept-Encoding', 'gzip,deflate'),
    NVPair('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13'), ]

headers0= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers1= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/login'), ]

headers2= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8000/oib/login'), ]

headers3= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://localhost:8000/oib/home;jsessionid=E696EE52ED37BD99EE3DE449983997A2'), ]

headers4= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://localhost:8000/oib/home;jsessionid=E696EE52ED37BD99EE3DE449983997A2'), ]

headers5= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'http://localhost:8000/oib/home;jsessionid=E696EE52ED37BD99EE3DE449983997A2'), ]

headers6= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/manage/manage_rubric.css'), ]

headers7= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8000/oib/home;jsessionid=E696EE52ED37BD99EE3DE449983997A2'), ]

headers8= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create'), ]

headers9= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create'), ]

headers10= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create'), ]

headers11= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/common/css/3p/jqueryMultiSelect.css'), ]

headers12= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create'), ]

headers13= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/assessment.css'), ]

headers14= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create'),
    NVPair('Cache-Control', 'no-cache'), ]

headers15= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/jquery-ui-1.7.2.custom.css'), ]

headers16= \
  [ NVPair('Accept', 'text/javascript, application/javascript, */*'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create'), ]

headers17= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/manage/manage.css'), ]

headers18= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create'), ]

headers19= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/common/css/skin.css'), ]

headers20= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui.css'), ]

headers21= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui_threetwelve.css'), ]

headers22= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/widgets/rounded_button.css'), ]

headers23= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create'),
    NVPair('Cache-Control', 'no-cache'), ]

headers24= \
  [ NVPair('Accept', 'text/javascript, text/html, application/xml, text/xml, */*'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create'),
    NVPair('Cache-Control', 'no-cache'), ]

headers25= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/common/css/basic.css'), ]

headers26= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create?id=1395'),
    NVPair('Cache-Control', 'no-cache'), ]

headers27= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8000/oib/assessment/create?id=1395'), ]

headers28= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/dashboard.css'), ]

headers29= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'http://localhost:8000/oib/home'), ]

headers30= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/manage/manage_assessment.css'), ]

headers31= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8000/oib/home'), ]

url0 = 'http://localhost:8000'
url1 = 'http://www.google-analytics.com:80'

# Create an HTTPRequest for each request, then replace the
# reference to the HTTPRequest with an instrumented version.
# You can access the unadorned instance using request101.__target__.
# Log in.
request101 = HTTPRequest(url=url0, headers=headers0)
request101 = Test(101, 'GET login').wrap(request101)

request102 = HTTPRequest(url=url0, headers=headers1)
request102 = Test(102, 'GET three2twelve.png').wrap(request102)

request201 = HTTPRequest(url=url0, headers=headers2)
request201 = Test(201, 'POST login').wrap(request201)

request202 = HTTPRequest(url=url0, headers=headers2)
request202 = Test(202, 'GET home').wrap(request202)

request203 = HTTPRequest(url=url0, headers=headers3)
request203 = Test(203, 'GET basic.css').wrap(request203)

request204 = HTTPRequest(url=url0, headers=headers3)
request204 = Test(204, 'GET skin.css').wrap(request204)

request205 = HTTPRequest(url=url0, headers=headers3)
request205 = Test(205, 'GET dashboard.css').wrap(request205)

request206 = HTTPRequest(url=url0, headers=headers3)
request206 = Test(206, 'GET styled_text.css').wrap(request206)

request207 = HTTPRequest(url=url0, headers=headers3)
request207 = Test(207, 'GET jquery-ui-1.7.2.custom.css').wrap(request207)

request208 = HTTPRequest(url=url0, headers=headers3)
request208 = Test(208, 'GET mClassNavBar.css').wrap(request208)

request209 = HTTPRequest(url=url0, headers=headers3)
request209 = Test(209, 'GET help.css').wrap(request209)

request210 = HTTPRequest(url=url0, headers=headers3)
request210 = Test(210, 'GET standards.css').wrap(request210)

request211 = HTTPRequest(url=url0, headers=headers3)
request211 = Test(211, 'GET manage.css').wrap(request211)

request212 = HTTPRequest(url=url0, headers=headers3)
request212 = Test(212, 'GET manage_item.css').wrap(request212)

request213 = HTTPRequest(url=url0, headers=headers3)
request213 = Test(213, 'GET GlobalNavBar.css').wrap(request213)

request214 = HTTPRequest(url=url0, headers=headers3)
request214 = Test(214, 'GET manage_passage.css').wrap(request214)

request215 = HTTPRequest(url=url0, headers=headers3)
request215 = Test(215, 'GET manage_assessment.css').wrap(request215)

request216 = HTTPRequest(url=url0, headers=headers3)
request216 = Test(216, 'GET manage_rubric.css').wrap(request216)

request217 = HTTPRequest(url=url0, headers=headers4)
request217 = Test(217, 'GET jquery-1.3.2.js').wrap(request217)

request218 = HTTPRequest(url=url0, headers=headers4)
request218 = Test(218, 'GET ui.core.js').wrap(request218)

request219 = HTTPRequest(url=url0, headers=headers4)
request219 = Test(219, 'GET ui.draggable.js').wrap(request219)

request220 = HTTPRequest(url=url0, headers=headers4)
request220 = Test(220, 'GET ui.sortable.js').wrap(request220)

request221 = HTTPRequest(url=url0, headers=headers4)
request221 = Test(221, 'GET closure.base.js').wrap(request221)

request222 = HTTPRequest(url=url0, headers=headers3)
request222 = Test(222, 'GET jqueryMultiSelect.css').wrap(request222)

request223 = HTTPRequest(url=url0, headers=headers3)
request223 = Test(223, 'GET view_entity.css').wrap(request223)

request224 = HTTPRequest(url=url0, headers=headers4)
request224 = Test(224, 'GET ui.resizable.js').wrap(request224)

request225 = HTTPRequest(url=url0, headers=headers4)
request225 = Test(225, 'GET ui.dialog.js').wrap(request225)

request226 = HTTPRequest(url=url0, headers=headers4)
request226 = Test(226, 'GET ui.slider.js').wrap(request226)

request227 = HTTPRequest(url=url0, headers=headers4)
request227 = Test(227, 'GET ui.tabs.js').wrap(request227)

request228 = HTTPRequest(url=url0, headers=headers4)
request228 = Test(228, 'GET jquery.tooltip.js').wrap(request228)

request229 = HTTPRequest(url=url0, headers=headers4)
request229 = Test(229, 'GET prototype.js').wrap(request229)

request230 = HTTPRequest(url=url0, headers=headers4)
request230 = Test(230, 'GET jquery_setup.js').wrap(request230)

request231 = HTTPRequest(url=url0, headers=headers4)
request231 = Test(231, 'GET jquery.form.js').wrap(request231)

request232 = HTTPRequest(url=url0, headers=headers4)
request232 = Test(232, 'GET math-utilities.js').wrap(request232)

request233 = HTTPRequest(url=url0, headers=headers4)
request233 = Test(233, 'GET jsonStringify.js').wrap(request233)

request234 = HTTPRequest(url=url0, headers=headers4)
request234 = Test(234, 'GET LaTeXMathML.js').wrap(request234)

request235 = HTTPRequest(url=url0, headers=headers4)
request235 = Test(235, 'GET autoresize.jquery.min.js').wrap(request235)

request236 = HTTPRequest(url=url0, headers=headers4)
request236 = Test(236, 'GET BackspaceSuppress.js').wrap(request236)

request237 = HTTPRequest(url=url0, headers=headers4)
request237 = Test(237, 'GET TimeoutDetect.js').wrap(request237)

request238 = HTTPRequest(url=url0, headers=headers4)
request238 = Test(238, 'GET standards.js').wrap(request238)

request239 = HTTPRequest(url=url0, headers=headers4)
request239 = Test(239, 'GET standardsUi.js').wrap(request239)

request240 = HTTPRequest(url=url0, headers=headers4)
request240 = Test(240, 'GET help.js').wrap(request240)

request241 = HTTPRequest(url=url0, headers=headers4)
request241 = Test(241, 'GET RoboHelp_CSH.js').wrap(request241)

request242 = HTTPRequest(url=url0, headers=headers4)
request242 = Test(242, 'GET wgen.oib.utilities.js').wrap(request242)

request243 = HTTPRequest(url=url0, headers=headers4)
request243 = Test(243, 'GET global_ready.js').wrap(request243)

request244 = HTTPRequest(url=url0, headers=headers4)
request244 = Test(244, 'GET googleAnalytics.js').wrap(request244)

request245 = HTTPRequest(url=url0, headers=headers4)
request245 = Test(245, 'GET cookieHandler.js').wrap(request245)

request246 = HTTPRequest(url=url0, headers=headers4)
request246 = Test(246, 'GET jquery_functions.js').wrap(request246)

request247 = HTTPRequest(url=url0, headers=headers4)
request247 = Test(247, 'GET sharing.js').wrap(request247)

request248 = HTTPRequest(url=url0, headers=headers4)
request248 = Test(248, 'GET tooltip.js').wrap(request248)

request249 = HTTPRequest(url=url0, headers=headers4)
request249 = Test(249, 'GET EntityPopupSourceUI.js').wrap(request249)

request250 = HTTPRequest(url=url0, headers=headers4)
request250 = Test(250, 'GET viewStandardsUi.js').wrap(request250)

request251 = HTTPRequest(url=url0, headers=headers4)
request251 = Test(251, 'GET ManageBrowser.js').wrap(request251)

request252 = HTTPRequest(url=url0, headers=headers4)
request252 = Test(252, 'GET ManagePassageBrowserRenderer.js').wrap(request252)

request253 = HTTPRequest(url=url0, headers=headers4)
request253 = Test(253, 'GET ManageItemBrowserRenderer.js').wrap(request253)

request254 = HTTPRequest(url=url0, headers=headers4)
request254 = Test(254, 'GET ViewItemBankEntity.js').wrap(request254)

request255 = HTTPRequest(url=url0, headers=headers4)
request255 = Test(255, 'GET SharingDropdown.js').wrap(request255)

request256 = HTTPRequest(url=url0, headers=headers4)
request256 = Test(256, 'GET createStandardsUi.js').wrap(request256)

request257 = HTTPRequest(url=url0, headers=headers4)
request257 = Test(257, 'GET jqueryMultiSelect.js').wrap(request257)

request258 = HTTPRequest(url=url0, headers=headers4)
request258 = Test(258, 'GET ManageBrowserRenderer.js').wrap(request258)

request259 = HTTPRequest(url=url0, headers=headers4)
request259 = Test(259, 'GET ManageRubricBrowserRenderer.js').wrap(request259)

request260 = HTTPRequest(url=url0, headers=headers4)
request260 = Test(260, 'GET ManageAssessmentBrowserRenderer.js').wrap(request260)

request261 = HTTPRequest(url=url0, headers=headers4)
request261 = Test(261, 'GET RecentEntityWidget.js').wrap(request261)

request262 = HTTPRequest(url=url0, headers=headers4)
request262 = Test(262, 'GET DashboardPage.js').wrap(request262)

request263 = HTTPRequest(url=url0, headers=headers4)
request263 = Test(263, 'GET dashboard_ready.js').wrap(request263)

request264 = HTTPRequest(url=url0, headers=headers4)
request264 = Test(264, 'GET QuestionType.js').wrap(request264)

request265 = HTTPRequest(url=url0, headers=headers4)
request265 = Test(265, 'GET OpenResponseQuestionType.js').wrap(request265)

request266 = HTTPRequest(url=url0, headers=headers4)
request266 = Test(266, 'GET GlobalNavBar.js').wrap(request266)

request301 = HTTPRequest(url=url1, headers=headers4)
request301 = Test(301, 'GET ga.js').wrap(request301)

request401 = HTTPRequest(url=url0, headers=headers5)
request401 = Test(401, 'GET recent').wrap(request401)

request501 = HTTPRequest(url=url0, headers=headers0)
request501 = Test(501, 'GET ellipsis.xml').wrap(request501)

request502 = HTTPRequest(url=url0, headers=headers6)
request502 = Test(502, 'GET locate_rounded_corner_objects.png').wrap(request502)

# Assessments > Create Assessment
request601 = HTTPRequest(url=url0, headers=headers7)
request601 = Test(601, 'GET create').wrap(request601)

request602 = HTTPRequest(url=url0, headers=headers8)
request602 = Test(602, 'GET rounded_button.css').wrap(request602)

request603 = HTTPRequest(url=url0, headers=headers8)
request603 = Test(603, 'GET assessment.css').wrap(request603)

request604 = HTTPRequest(url=url0, headers=headers9)
request604 = Test(604, 'GET tooltip_win_arrow_top.png').wrap(request604)

request701 = HTTPRequest(url=url0, headers=headers10)
request701 = Test(701, 'GET empty.html').wrap(request701)

request702 = HTTPRequest(url=url0, headers=headers11)
request702 = Test(702, 'GET dropdown_top_bottom_sprite.png').wrap(request702)

request703 = HTTPRequest(url=url0, headers=headers11)
request703 = Test(703, 'GET dropdown_sides.png').wrap(request703)

request704 = HTTPRequest(url=url0, headers=headers12)
request704 = Test(704, 'GET tiny_mce.js').wrap(request704)

request705 = HTTPRequest(url=url0, headers=headers12)
request705 = Test(705, 'GET threetwelveImage.js').wrap(request705)

request706 = HTTPRequest(url=url0, headers=headers12)
request706 = Test(706, 'GET SubjectDropdown.js').wrap(request706)

request707 = HTTPRequest(url=url0, headers=headers12)
request707 = Test(707, 'GET EditPageSubjectDropdown.js').wrap(request707)

request708 = HTTPRequest(url=url0, headers=headers12)
request708 = Test(708, 'GET tooltip.js').wrap(request708)

request709 = HTTPRequest(url=url0, headers=headers12)
request709 = Test(709, 'GET EditPage.js').wrap(request709)

request710 = HTTPRequest(url=url0, headers=headers12)
request710 = Test(710, 'GET Ajax.js').wrap(request710)

request711 = HTTPRequest(url=url0, headers=headers12)
request711 = Test(711, 'GET StyledTextEditor.js').wrap(request711)

request712 = HTTPRequest(url=url0, headers=headers12)
request712 = Test(712, 'GET AssessmentBodyJSONTranslator.js').wrap(request712)

request713 = HTTPRequest(url=url0, headers=headers12)
request713 = Test(713, 'GET AssessmentComponentType.js').wrap(request713)

request714 = HTTPRequest(url=url0, headers=headers12)
request714 = Test(714, 'GET ComponentAdder.js').wrap(request714)

request715 = HTTPRequest(url=url0, headers=headers12)
request715 = Test(715, 'GET EditAssessmentPage.js').wrap(request715)

request716 = HTTPRequest(url=url0, headers=headers12)
request716 = Test(716, 'GET dialog.js').wrap(request716)

request717 = HTTPRequest(url=url0, headers=headers12)
request717 = Test(717, 'GET StyledTextPopup.js').wrap(request717)

request718 = HTTPRequest(url=url0, headers=headers13)
request718 = Test(718, 'GET hr_grey.png').wrap(request718)

request719 = HTTPRequest(url=url0, headers=headers12)
request719 = Test(719, 'GET PassageBrowser.js').wrap(request719)

request720 = HTTPRequest(url=url0, headers=headers13)
request720 = Test(720, 'GET rounded_corner_white_vert.png').wrap(request720)

request721 = HTTPRequest(url=url0, headers=headers12)
request721 = Test(721, 'GET MultipleChoiceQuestionType.js').wrap(request721)

request722 = HTTPRequest(url=url0, headers=headers12)
request722 = Test(722, 'GET SelectEntityPopup.js').wrap(request722)

request723 = HTTPRequest(url=url0, headers=headers12)
request723 = Test(723, 'GET ItemBrowser.js').wrap(request723)

request724 = HTTPRequest(url=url0, headers=headers12)
request724 = Test(724, 'GET new_assessment_ready.js').wrap(request724)

request725 = HTTPRequest(url=url0, headers=headers13)
request725 = Test(725, 'GET rounded_corner_white_horiz.png').wrap(request725)

request726 = HTTPRequest(url=url0, headers=headers13)
request726 = Test(726, 'GET rounded_corner_white.png').wrap(request726)

# Add title.
# Click 'Add Item(s)'.
request801 = HTTPRequest(url=url0, headers=headers14)
request801 = Test(801, 'POST assessments').wrap(request801)

request802 = HTTPRequest(url=url0, headers=headers15)
request802 = Test(802, 'GET border.png').wrap(request802)

request803 = HTTPRequest(url=url0, headers=headers15)
request803 = Test(803, 'GET close_X.png').wrap(request803)

request901 = HTTPRequest(url=url0, headers=headers12)
request901 = Test(901, 'GET manage').wrap(request901)

request902 = HTTPRequest(url=url0, headers=headers9)
request902 = Test(902, 'GET red_cancel_icon.png').wrap(request902)

request903 = HTTPRequest(url=url0, headers=headers9)
request903 = Test(903, 'GET search_within_bttn.png').wrap(request903)

request904 = HTTPRequest(url=url0, headers=headers16)
request904 = Test(904, 'GET ViewItemBankEntity.js').wrap(request904)

request905 = HTTPRequest(url=url0, headers=headers17)
request905 = Test(905, 'GET left_pane_background.png').wrap(request905)

request906 = HTTPRequest(url=url0, headers=headers17)
request906 = Test(906, 'GET search_within_glass.png').wrap(request906)

request907 = HTTPRequest(url=url0, headers=headers17)
request907 = Test(907, 'GET locate_stroke_quantity_results_bg.png').wrap(request907)

request908 = HTTPRequest(url=url0, headers=headers17)
request908 = Test(908, 'GET locate_tab_arrows.png').wrap(request908)

request909 = HTTPRequest(url=url0, headers=headers16)
request909 = Test(909, 'GET sharing.js').wrap(request909)

request910 = HTTPRequest(url=url0, headers=headers16)
request910 = Test(910, 'GET createStandardsUi.js').wrap(request910)

request911 = HTTPRequest(url=url0, headers=headers16)
request911 = Test(911, 'GET viewStandardsUi.js').wrap(request911)

request912 = HTTPRequest(url=url0, headers=headers16)
request912 = Test(912, 'GET tooltip.js').wrap(request912)

request913 = HTTPRequest(url=url0, headers=headers16)
request913 = Test(913, 'GET AssignmentCreator.js').wrap(request913)

request914 = HTTPRequest(url=url0, headers=headers16)
request914 = Test(914, 'GET EntityPopupSourceUI.js').wrap(request914)

request915 = HTTPRequest(url=url0, headers=headers16)
request915 = Test(915, 'GET ManageBrowser.js').wrap(request915)

request916 = HTTPRequest(url=url0, headers=headers16)
request916 = Test(916, 'GET ManageBrowserRenderer.js').wrap(request916)

request917 = HTTPRequest(url=url0, headers=headers16)
request917 = Test(917, 'GET ManageItemBrowserRenderer.js').wrap(request917)

request918 = HTTPRequest(url=url0, headers=headers16)
request918 = Test(918, 'GET ManageStandardsUi.js').wrap(request918)

request919 = HTTPRequest(url=url0, headers=headers16)
request919 = Test(919, 'GET AssessmentFilterWidget.js').wrap(request919)

request920 = HTTPRequest(url=url0, headers=headers16)
request920 = Test(920, 'GET ManageFilterWidget.js').wrap(request920)

request921 = HTTPRequest(url=url0, headers=headers16)
request921 = Test(921, 'GET QuestionType.js').wrap(request921)

request922 = HTTPRequest(url=url0, headers=headers16)
request922 = Test(922, 'GET OpenResponseQuestionType.js').wrap(request922)

request923 = HTTPRequest(url=url0, headers=headers16)
request923 = Test(923, 'GET SubjectDropdown.js').wrap(request923)

request924 = HTTPRequest(url=url0, headers=headers16)
request924 = Test(924, 'GET EditPageSubjectDropdown.js').wrap(request924)

request925 = HTTPRequest(url=url0, headers=headers16)
request925 = Test(925, 'GET jqueryMultiSelect.js').wrap(request925)

request926 = HTTPRequest(url=url0, headers=headers16)
request926 = Test(926, 'GET manage_ready.js').wrap(request926)

request1001 = HTTPRequest(url=url0, headers=headers18)
request1001 = Test(1001, 'GET myStandardsRootNodes').wrap(request1001)

request1101 = HTTPRequest(url=url0, headers=headers18)
request1101 = Test(1101, 'GET getAll').wrap(request1101)

request1102 = HTTPRequest(url=url0, headers=headers17)
request1102 = Test(1102, 'GET standards_bullet_image.png').wrap(request1102)

request1201 = HTTPRequest(url=url0, headers=headers12)
request1201 = Test(1201, 'GET keepalive').wrap(request1201)

# Filter by standard.
request1301 = HTTPRequest(url=url0, headers=headers18)
request1301 = Test(1301, 'GET standardsTree').wrap(request1301)

request1401 = HTTPRequest(url=url0, headers=headers18)
request1401 = Test(1401, 'GET alignedToSubtree').wrap(request1401)

request1501 = HTTPRequest(url=url0, headers=headers18)
request1501 = Test(1501, 'GET standardsTreeGrandkids').wrap(request1501)

request1601 = HTTPRequest(url=url0, headers=headers18)
request1601 = Test(1601, 'GET alignedToSubtree').wrap(request1601)

request1701 = HTTPRequest(url=url0, headers=headers18)
request1701 = Test(1701, 'GET standardsTreeGrandkids').wrap(request1701)

request1801 = HTTPRequest(url=url0, headers=headers18)
request1801 = Test(1801, 'GET alignedToSubtree').wrap(request1801)

request1901 = HTTPRequest(url=url0, headers=headers18)
request1901 = Test(1901, 'GET standardsTreeGrandkids').wrap(request1901)

request2001 = HTTPRequest(url=url0, headers=headers18)
request2001 = Test(2001, 'GET alignedToSubtree').wrap(request2001)

request2101 = HTTPRequest(url=url0, headers=headers18)
request2101 = Test(2101, 'GET alignedToSubtree').wrap(request2101)

request2201 = HTTPRequest(url=url0, headers=headers18)
request2201 = Test(2201, 'GET alignedToNode').wrap(request2201)

# Select standard.
request2301 = HTTPRequest(url=url0, headers=headers14)
request2301 = Test(2301, 'POST add').wrap(request2301)

request2401 = HTTPRequest(url=url0, headers=headers12)
request2401 = Test(2401, 'GET keepalive').wrap(request2401)

# Click 'Attach Items'.
request2402 = HTTPRequest(url=url0, headers=headers13)
request2402 = Test(2402, 'GET rounded_corner_yellow_vert_bg.png').wrap(request2402)

request2403 = HTTPRequest(url=url0, headers=headers13)
request2403 = Test(2403, 'GET rounded_corner_yellow_top.png').wrap(request2403)

request2404 = HTTPRequest(url=url0, headers=headers19)
request2404 = Test(2404, 'GET icons_actions.gif').wrap(request2404)

request2405 = HTTPRequest(url=url0, headers=headers13)
request2405 = Test(2405, 'GET rounded_corner_yellow_horiz_bg.png').wrap(request2405)

request2406 = HTTPRequest(url=url0, headers=headers13)
request2406 = Test(2406, 'GET rounded_corner_yellow_top_ffffd1.png').wrap(request2406)

request2501 = HTTPRequest(url=url0, headers=headers14)
request2501 = Test(2501, 'POST assessments').wrap(request2501)

# Click 'Add Passage(s)'.
request2601 = HTTPRequest(url=url0, headers=headers14)
request2601 = Test(2601, 'POST assessments').wrap(request2601)

request2701 = HTTPRequest(url=url0, headers=headers12)
request2701 = Test(2701, 'GET manage').wrap(request2701)

request2702 = HTTPRequest(url=url0, headers=headers16)
request2702 = Test(2702, 'GET ViewItemBankEntity.js').wrap(request2702)

request2703 = HTTPRequest(url=url0, headers=headers16)
request2703 = Test(2703, 'GET sharing.js').wrap(request2703)

request2704 = HTTPRequest(url=url0, headers=headers16)
request2704 = Test(2704, 'GET createStandardsUi.js').wrap(request2704)

request2705 = HTTPRequest(url=url0, headers=headers16)
request2705 = Test(2705, 'GET viewStandardsUi.js').wrap(request2705)

request2706 = HTTPRequest(url=url0, headers=headers16)
request2706 = Test(2706, 'GET tooltip.js').wrap(request2706)

request2707 = HTTPRequest(url=url0, headers=headers16)
request2707 = Test(2707, 'GET AssignmentCreator.js').wrap(request2707)

request2708 = HTTPRequest(url=url0, headers=headers16)
request2708 = Test(2708, 'GET EntityPopupSourceUI.js').wrap(request2708)

request2709 = HTTPRequest(url=url0, headers=headers16)
request2709 = Test(2709, 'GET ManageBrowser.js').wrap(request2709)

request2710 = HTTPRequest(url=url0, headers=headers16)
request2710 = Test(2710, 'GET ManageBrowserRenderer.js').wrap(request2710)

request2711 = HTTPRequest(url=url0, headers=headers16)
request2711 = Test(2711, 'GET ManagePassageBrowserRenderer.js').wrap(request2711)

request2712 = HTTPRequest(url=url0, headers=headers16)
request2712 = Test(2712, 'GET ManageStandardsUi.js').wrap(request2712)

request2713 = HTTPRequest(url=url0, headers=headers16)
request2713 = Test(2713, 'GET AssessmentFilterWidget.js').wrap(request2713)

request2714 = HTTPRequest(url=url0, headers=headers16)
request2714 = Test(2714, 'GET ManageFilterWidget.js').wrap(request2714)

request2715 = HTTPRequest(url=url0, headers=headers16)
request2715 = Test(2715, 'GET QuestionType.js').wrap(request2715)

request2716 = HTTPRequest(url=url0, headers=headers16)
request2716 = Test(2716, 'GET OpenResponseQuestionType.js').wrap(request2716)

request2717 = HTTPRequest(url=url0, headers=headers16)
request2717 = Test(2717, 'GET SubjectDropdown.js').wrap(request2717)

request2718 = HTTPRequest(url=url0, headers=headers16)
request2718 = Test(2718, 'GET EditPageSubjectDropdown.js').wrap(request2718)

request2719 = HTTPRequest(url=url0, headers=headers16)
request2719 = Test(2719, 'GET jqueryMultiSelect.js').wrap(request2719)

request2720 = HTTPRequest(url=url0, headers=headers16)
request2720 = Test(2720, 'GET manage_ready.js').wrap(request2720)

request2801 = HTTPRequest(url=url0, headers=headers18)
request2801 = Test(2801, 'GET myStandardsRootNodes').wrap(request2801)

request2901 = HTTPRequest(url=url0, headers=headers18)
request2901 = Test(2901, 'GET getAll').wrap(request2901)

request3001 = HTTPRequest(url=url0, headers=headers12)
request3001 = Test(3001, 'GET keepalive').wrap(request3001)

# Search for 'body'.
request3101 = HTTPRequest(url=url0, headers=headers18)
request3101 = Test(3101, 'GET getAll').wrap(request3101)

# Filter to 'OIB'.
request3201 = HTTPRequest(url=url0, headers=headers18)
request3201 = Test(3201, 'GET getAll').wrap(request3201)

request3301 = HTTPRequest(url=url0, headers=headers12)
request3301 = Test(3301, 'GET keepalive').wrap(request3301)

# Select first passage.
request3401 = HTTPRequest(url=url0, headers=headers14)
request3401 = Test(3401, 'POST add').wrap(request3401)

# Click 'Attach Passages'.
request3402 = HTTPRequest(url=url0, headers=headers13)
request3402 = Test(3402, 'GET rounded_corner_yellow_vert.png').wrap(request3402)

request3403 = HTTPRequest(url=url0, headers=headers13)
request3403 = Test(3403, 'GET rounded_corner_yellow_horiz.png').wrap(request3403)

request3501 = HTTPRequest(url=url0, headers=headers14)
request3501 = Test(3501, 'POST assessments').wrap(request3501)

# Click 'Preview'.
request3502 = HTTPRequest(url=url0, headers=headers15)
request3502 = Test(3502, 'GET buttons.png').wrap(request3502)

# Click 'Test Booklet'.
request3601 = HTTPRequest(url=url0, headers=headers10)
request3601 = Test(3601, 'POST studentTest').wrap(request3601)

request3701 = HTTPRequest(url=url0, headers=headers12)
request3701 = Test(3701, 'GET keepalive').wrap(request3701)

# Close overlay.
# Click 'Add Directions'.
request3702 = HTTPRequest(url=url0, headers=headers12)
request3702 = Test(3702, 'GET en.js').wrap(request3702)

request3703 = HTTPRequest(url=url0, headers=headers12)
request3703 = Test(3703, 'GET editor_template.js').wrap(request3703)

request3704 = HTTPRequest(url=url0, headers=headers12)
request3704 = Test(3704, 'GET editor_plugin.js').wrap(request3704)

request3705 = HTTPRequest(url=url0, headers=headers12)
request3705 = Test(3705, 'GET editor_plugin.js').wrap(request3705)

request3706 = HTTPRequest(url=url0, headers=headers12)
request3706 = Test(3706, 'GET editor_plugin.js').wrap(request3706)

request3707 = HTTPRequest(url=url0, headers=headers12)
request3707 = Test(3707, 'GET editor_plugin.js').wrap(request3707)

request3708 = HTTPRequest(url=url0, headers=headers12)
request3708 = Test(3708, 'GET editor_plugin.js').wrap(request3708)

request3709 = HTTPRequest(url=url0, headers=headers12)
request3709 = Test(3709, 'GET editor_plugin.js').wrap(request3709)

request3710 = HTTPRequest(url=url0, headers=headers12)
request3710 = Test(3710, 'GET editor_plugin.js').wrap(request3710)

request3711 = HTTPRequest(url=url0, headers=headers12)
request3711 = Test(3711, 'GET editor_plugin.js').wrap(request3711)

request3712 = HTTPRequest(url=url0, headers=headers12)
request3712 = Test(3712, 'GET editor_plugin.js').wrap(request3712)

request3713 = HTTPRequest(url=url0, headers=headers12)
request3713 = Test(3713, 'GET editor_plugin.js').wrap(request3713)

request3714 = HTTPRequest(url=url0, headers=headers12)
request3714 = Test(3714, 'GET en.js').wrap(request3714)

request3715 = HTTPRequest(url=url0, headers=headers8)
request3715 = Test(3715, 'GET ui.css').wrap(request3715)

request3716 = HTTPRequest(url=url0, headers=headers8)
request3716 = Test(3716, 'GET ui_threetwelve.css').wrap(request3716)

request3717 = HTTPRequest(url=url0, headers=headers8)
request3717 = Test(3717, 'GET window.css').wrap(request3717)

request3718 = HTTPRequest(url=url0, headers=headers20)
request3718 = Test(3718, 'GET button_bg.png').wrap(request3718)

request3719 = HTTPRequest(url=url0, headers=headers20)
request3719 = Test(3719, 'GET icons.gif').wrap(request3719)

request3720 = HTTPRequest(url=url0, headers=headers21)
request3720 = Test(3720, 'GET small.png').wrap(request3720)

request3721 = HTTPRequest(url=url0, headers=headers21)
request3721 = Test(3721, 'GET large.png').wrap(request3721)

request3722 = HTTPRequest(url=url0, headers=headers21)
request3722 = Test(3722, 'GET medium.png').wrap(request3722)

request3723 = HTTPRequest(url=url0, headers=headers21)
request3723 = Test(3723, 'GET ed_mathformula.gif').wrap(request3723)

request3724 = HTTPRequest(url=url0, headers=headers21)
request3724 = Test(3724, 'GET btn_wysiwyg_space_title_2.gif').wrap(request3724)

request3725 = HTTPRequest(url=url0, headers=headers21)
request3725 = Test(3725, 'GET btn_wysiwyg_space_title_1.gif').wrap(request3725)

request3726 = HTTPRequest(url=url0, headers=headers21)
request3726 = Test(3726, 'GET btn_wysiwyg_space_title_3.gif').wrap(request3726)

request3727 = HTTPRequest(url=url0, headers=headers21)
request3727 = Test(3727, 'GET btn_wysiwyg_add_space_ruled.png').wrap(request3727)

request3728 = HTTPRequest(url=url0, headers=headers21)
request3728 = Test(3728, 'GET btn_wysiwyg_add_space_unruled.png').wrap(request3728)

request3729 = HTTPRequest(url=url0, headers=headers8)
request3729 = Test(3729, 'GET content.css').wrap(request3729)

# Add directions text.
request3801 = HTTPRequest(url=url0, headers=headers14)
request3801 = Test(3801, 'POST add').wrap(request3801)

request3901 = HTTPRequest(url=url0, headers=headers12)
request3901 = Test(3901, 'GET keepalive').wrap(request3901)

# Click 'Proctor Directions'.
# Add proctor directions text.
request4001 = HTTPRequest(url=url0, headers=headers14)
request4001 = Test(4001, 'POST add').wrap(request4001)

# Click 'Page Break'.
request4101 = HTTPRequest(url=url0, headers=headers14)
request4101 = Test(4101, 'POST add').wrap(request4101)

request4102 = HTTPRequest(url=url0, headers=headers9)
request4102 = Test(4102, 'GET icon_page_break.png').wrap(request4102)

# Add 'Stop'.
request4201 = HTTPRequest(url=url0, headers=headers14)
request4201 = Test(4201, 'POST add').wrap(request4201)

request4202 = HTTPRequest(url=url0, headers=headers9)
request4202 = Test(4202, 'GET icon_stop.png').wrap(request4202)

request4301 = HTTPRequest(url=url0, headers=headers12)
request4301 = Test(4301, 'GET keepalive').wrap(request4301)

# Move 'Stop'.
request4302 = HTTPRequest(url=url0, headers=headers22)
request4302 = Test(4302, 'GET button_save_preview_90dcfc.png').wrap(request4302)

# Click 'Preview'.
# Close overlay.
# Save assessment.
request4401 = HTTPRequest(url=url0, headers=headers12)
request4401 = Test(4401, 'GET keepalive').wrap(request4401)

request4501 = HTTPRequest(url=url0, headers=headers23)
request4501 = Test(4501, 'POST sharingAgreement').wrap(request4501)

# Click 'I Agree'.
request4601 = HTTPRequest(url=url0, headers=headers24)
request4601 = Test(4601, 'POST save').wrap(request4601)

request4602 = HTTPRequest(url=url0, headers=headers25)
request4602 = Test(4602, 'GET create_box_top.png').wrap(request4602)

request4603 = HTTPRequest(url=url0, headers=headers25)
request4603 = Test(4603, 'GET create_box_bkgrd.png').wrap(request4603)

request4604 = HTTPRequest(url=url0, headers=headers25)
request4604 = Test(4604, 'GET create_box_bottom.png').wrap(request4604)

# Edit Assessment
request4701 = HTTPRequest(url=url0, headers=headers10)
request4701 = Test(4701, 'GET create').wrap(request4701)

request4801 = HTTPRequest(url=url0, headers=headers26)
request4801 = Test(4801, 'POST assessments').wrap(request4801)

# Click 'Cancel'.
request4901 = HTTPRequest(url=url0, headers=headers27)
request4901 = Test(4901, 'GET home').wrap(request4901)

request4902 = HTTPRequest(url=url0, headers=headers28)
request4902 = Test(4902, 'GET video_box_gradient.png').wrap(request4902)

request5001 = HTTPRequest(url=url0, headers=headers29)
request5001 = Test(5001, 'GET recent').wrap(request5001)

request5002 = HTTPRequest(url=url0, headers=headers30)
request5002 = Test(5002, 'GET sprites.png').wrap(request5002)

request5003 = HTTPRequest(url=url0, headers=headers30)
request5003 = Test(5003, 'GET assessment_item_count_box.png').wrap(request5003)

# Log out.
request5101 = HTTPRequest(url=url0, headers=headers31)
request5101 = Test(5101, 'GET logout').wrap(request5101)

request5102 = HTTPRequest(url=url0, headers=headers31)
request5102 = Test(5102, 'GET Logout.do').wrap(request5102)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET login (requests 101-102)."""
    result = request101.GET('/oib/login')

    grinder.sleep(22)
    request102.GET('/oib/static/images/three2twelve.png')

    return result

  def page2(self):
    """POST login (requests 201-266)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request201.POST('/oib/login',
      ( NVPair('username', 'demoCA100105'),
        NVPair('password', ''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))
    self.token_jsessionid = \
      httpUtilities.valueFromLocationURI('jsessionid') # 'E696EE52ED37BD99EE3DE449983997A2'

    grinder.sleep(35)
    request202.GET('/oib/home;jsessionid=' +
      self.token_jsessionid)

    grinder.sleep(29)
    request203.GET('/oib/static/common/css/basic.css')

    request204.GET('/oib/static/common/css/skin.css')

    request205.GET('/oib/static/css/dashboard.css')

    request206.GET('/oib/static/css/styled_text.css')

    request207.GET('/oib/static/css/jquery-ui-1.7.2.custom.css')

    request208.GET('/oib/static/common/css/widgets/mClassNavBar.css')

    request209.GET('/oib/static/css/widgets/help.css')

    request210.GET('/oib/static/css/standards.css')

    request211.GET('/oib/static/css/manage/manage.css')

    request212.GET('/oib/static/css/manage/manage_item.css')

    request213.GET('/oib/static/common/css/widgets/GlobalNavBar.css')

    request214.GET('/oib/static/css/manage/manage_passage.css')

    request215.GET('/oib/static/css/manage/manage_assessment.css')

    request216.GET('/oib/static/css/manage/manage_rubric.css')

    request217.GET('/oib/static/common/js/3p/jquery-1.3.2.js')

    request218.GET('/oib/static/common/js/3p/jqueryui/ui.core.js')

    request219.GET('/oib/static/common/js/3p/jqueryui/ui.draggable.js')

    request220.GET('/oib/static/common/js/3p/jqueryui/ui.sortable.js')

    request221.GET('/oib/static/common/js/3p/closure.base.js')

    request222.GET('/oib/static/common/css/3p/jqueryMultiSelect.css')

    request223.GET('/oib/static/css/view_entity.css')

    request224.GET('/oib/static/common/js/3p/jqueryui/ui.resizable.js')

    request225.GET('/oib/static/common/js/3p/jqueryui/ui.dialog.js')

    request226.GET('/oib/static/common/js/3p/jqueryui/ui.slider.js')

    request227.GET('/oib/static/common/js/3p/jqueryui/ui.tabs.js')

    request228.GET('/oib/static/common/js/3p/jquery.tooltip.js')

    request229.GET('/oib/static/common/js/3p/prototype.js')

    request230.GET('/oib/static/common/js/jquery_setup.js')

    request231.GET('/oib/static/common/js/3p/jquery.form.js')

    request232.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/js/math-utilities.js')

    request233.GET('/oib/static/common/js/3p/jsonStringify.js')

    request234.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/js/LaTeXMathML.js')

    request235.GET('/oib/static/common/js/3p/autoresize.jquery.min.js')

    request236.GET('/oib/static/common/js/widgets/BackspaceSuppress.js')

    request237.GET('/oib/static/common/js/widgets/TimeoutDetect.js')

    request238.GET('/oib/static/js/standardsBrowser/standards.js')

    request239.GET('/oib/static/js/standardsBrowser/standardsUi.js')

    request240.GET('/oib/static/common/js/widgets/help.js')

    request241.GET('/oib/static/common/js/3p/RoboHelp_CSH.js')

    request242.GET('/oib/static/js/wgen.oib.utilities.js')

    request243.GET('/oib/static/js/global_ready.js')

    request244.GET('/oib/static/common/js/3p/googleAnalytics.js')

    request245.GET('/oib/static/js/cookieHandler.js')

    request246.GET('/oib/static/js/jquery_functions.js')

    request247.GET('/oib/static/js/widgets/sharing.js')

    request248.GET('/oib/static/js/widgets/tooltip.js')

    request249.GET('/oib/static/js/EntityPopupSourceUI.js')

    request250.GET('/oib/static/js/standardsBrowser/viewStandardsUi.js')

    request251.GET('/oib/static/js/manage/ManageBrowser.js')

    request252.GET('/oib/static/js/manage/ManagePassageBrowserRenderer.js')

    request253.GET('/oib/static/js/manage/ManageItemBrowserRenderer.js')

    request254.GET('/oib/static/js/ViewItemBankEntity.js')

    request255.GET('/oib/static/js/widgets/SharingDropdown.js')

    request256.GET('/oib/static/js/standardsBrowser/createStandardsUi.js')

    request257.GET('/oib/static/common/js/3p/jqueryMultiSelect.js')

    request258.GET('/oib/static/js/manage/ManageBrowserRenderer.js')

    grinder.sleep(191)
    request259.GET('/oib/static/js/manage/ManageRubricBrowserRenderer.js')

    request260.GET('/oib/static/js/manage/ManageAssessmentBrowserRenderer.js')

    request261.GET('/oib/static/js/dashboard/widgets/RecentEntityWidget.js')

    request262.GET('/oib/static/js/dashboard/DashboardPage.js')

    request263.GET('/oib/static/js/dashboard/dashboard_ready.js')

    request264.GET('/oib/static/js/item/question/QuestionType.js')

    request265.GET('/oib/static/js/item/question/OpenResponseQuestionType.js')

    request266.GET('/oib/static/common/js/widgets/GlobalNavBar.js')

    return result

  def page3(self):
    """GET ga.js (request 301)."""
    result = request301.GET('/ga.js')

    return result

  def page4(self):
    """GET recent (request 401)."""
    self.token_type = \
      'all'
    self.token_pageSize = \
      '50'
    self.token_page = \
      '0'
    self.token__ = \
      '1295889551106'
    result = request401.GET('/oib/webservices/entities/recent' +
      '?type=' +
      self.token_type +
      '&pageSize=' +
      self.token_pageSize +
      '&page=' +
      self.token_page +
      '&_=' +
      self.token__)

    return result

  def page5(self):
    """GET ellipsis.xml (requests 501-502)."""
    result = request501.GET('/oib/static/common/css/ellipsis.xml')

    grinder.sleep(42)
    request502.GET('/oib/static/images/manage/locate_rounded_corner_objects.png')

    return result

  def page6(self):
    """GET create (requests 601-604)."""
    result = request601.GET('/oib/assessment/create')

    grinder.sleep(43)
    request602.GET('/oib/static/css/widgets/rounded_button.css')

    grinder.sleep(18)
    request603.GET('/oib/static/css/assessment.css')

    request604.GET('/oib/static/images/tooltips/tooltip_win_arrow_top.png')

    return result

  def page7(self):
    """GET empty.html (requests 701-726)."""
    result = request701.GET('/oib/static/empty.html')

    request702.GET('/oib/static/images/sprites/dropdown_top_bottom_sprite.png')

    request703.GET('/oib/static/images/sprites/dropdown_sides.png')

    grinder.sleep(49)
    request704.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/tiny_mce.js')

    request705.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelveimage/js/threetwelveImage.js')

    request706.GET('/oib/static/js/widgets/SubjectDropdown.js')

    request707.GET('/oib/static/js/widgets/EditPageSubjectDropdown.js')

    request708.GET('/oib/static/common/js/widgets/tooltip.js')

    request709.GET('/oib/static/js/EditPage.js')

    request710.GET('/oib/static/common/js/wgen/threetwelve/Ajax.js')

    request711.GET('/oib/static/js/StyledTextEditor.js')

    request712.GET('/oib/static/js/assessment/AssessmentBodyJSONTranslator.js')

    request713.GET('/oib/static/js/assessment/AssessmentComponentType.js')

    request714.GET('/oib/static/js/assessment/ComponentAdder.js')

    request715.GET('/oib/static/js/assessment/EditAssessmentPage.js')

    request716.GET('/oib/static/js/widgets/dialog.js')

    request717.GET('/oib/static/js/StyledTextPopup.js')

    request718.GET('/oib/static/images/assessment/hr_grey.png')

    request719.GET('/oib/static/js/assessment/PassageBrowser.js')

    request720.GET('/oib/static/images/assessment/rounded_corner_white_vert.png')

    request721.GET('/oib/static/js/item/question/MultipleChoiceQuestionType.js')

    request722.GET('/oib/static/js/SelectEntityPopup.js')

    request723.GET('/oib/static/js/assessment/ItemBrowser.js')

    request724.GET('/oib/static/js/new_assessment_ready.js')

    request725.GET('/oib/static/images/assessment/rounded_corner_white_horiz.png')

    request726.GET('/oib/static/images/assessment/rounded_corner_white.png')

    return result

  def page8(self):
    """POST assessments (requests 801-803)."""
    result = request801.POST('/oib/pools/list/assessments',
      ( NVPair('assessmentJSON', '{\"subject\": \"ELA\", \"title\": \"Load test assessment\", \"type\": \"ad_hoc\", \"delivery\": \"offline\", \"body\": {\"main_content\": [{\"type\": \"booklet\", \"title\": \"\", \"children\": []}]}}'),
        NVPair('poolId', '831'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    request802.GET('/oib/static/images/view_overlay/border.png')

    request803.GET('/oib/static/images/view_overlay/close_X.png')

    return result

  def page9(self):
    """GET manage (requests 901-926)."""
    self.token__ = \
      '1295889600938'
    self.token_subject = \
      'ELA'
    self.token_forSelect = \
      'true'
    self.token_isMultiSelect = \
      'true'
    result = request901.GET('/oib/item/manage' +
      '?_=' +
      self.token__ +
      '&subject=' +
      self.token_subject +
      '&forSelect=' +
      self.token_forSelect +
      '&isMultiSelect=' +
      self.token_isMultiSelect)

    grinder.sleep(21)
    request902.GET('/oib/static/images/manage/search/red_cancel_icon.png')

    request903.GET('/oib/static/images/manage/search/search_within_bttn.png')

    grinder.sleep(17)
    self.token__ = \
      '1295889601091'
    request904.GET('/oib/static/js/ViewItemBankEntity.js' +
      '?_=' +
      self.token__)

    grinder.sleep(21)
    request905.GET('/oib/static/images/manage/left_pane_background.png')

    request906.GET('/oib/static/images/manage/search/search_within_glass.png')

    request907.GET('/oib/static/images/manage/locate_stroke_quantity_results_bg.png')

    request908.GET('/oib/static/images/manage/locate_tab_arrows.png')

    grinder.sleep(18)
    self.token__ = \
      '1295889601148'
    request909.GET('/oib/static/js/widgets/sharing.js' +
      '?_=' +
      self.token__)

    grinder.sleep(128)
    self.token__ = \
      '1295889601278'
    request910.GET('/oib/static/js/standardsBrowser/createStandardsUi.js' +
      '?_=' +
      self.token__)

    grinder.sleep(22)
    self.token__ = \
      '1295889601303'
    request911.GET('/oib/static/js/standardsBrowser/viewStandardsUi.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601312'
    request912.GET('/oib/static/js/widgets/tooltip.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601317'
    request913.GET('/oib/static/js/widgets/AssignmentCreator.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601324'
    request914.GET('/oib/static/js/EntityPopupSourceUI.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601331'
    request915.GET('/oib/static/js/manage/ManageBrowser.js' +
      '?_=' +
      self.token__)

    grinder.sleep(22)
    self.token__ = \
      '1295889601366'
    request916.GET('/oib/static/js/manage/ManageBrowserRenderer.js' +
      '?_=' +
      self.token__)

    grinder.sleep(16)
    self.token__ = \
      '1295889601384'
    request917.GET('/oib/static/js/manage/ManageItemBrowserRenderer.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601390'
    request918.GET('/oib/static/js/standardsBrowser/ManageStandardsUi.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601400'
    request919.GET('/oib/static/js/manage/AssessmentFilterWidget.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601407'
    request920.GET('/oib/static/js/manage/ManageFilterWidget.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601416'
    request921.GET('/oib/static/js/item/question/QuestionType.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601427'
    request922.GET('/oib/static/js/item/question/OpenResponseQuestionType.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601436'
    request923.GET('/oib/static/js/widgets/SubjectDropdown.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601443'
    request924.GET('/oib/static/js/widgets/EditPageSubjectDropdown.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889601449'
    request925.GET('/oib/static/common/js/3p/jqueryMultiSelect.js' +
      '?_=' +
      self.token__)

    grinder.sleep(20)
    self.token__ = \
      '1295889601472'
    request926.GET('/oib/static/js/manage/manage_ready.js' +
      '?_=' +
      self.token__)

    return result

  def page10(self):
    """GET myStandardsRootNodes (request 1001)."""
    self.token__ = \
      '1295889601544'
    self.token_echo = \
      '0'
    self.token_getAlignCount = \
      'true'
    result = request1001.GET('/oib/standards/item/myStandardsRootNodes' +
      '?_=' +
      self.token__ +
      '&echo=' +
      self.token_echo +
      '&getAlignCount=' +
      self.token_getAlignCount +
      '&subject=' +
      self.token_subject)

    return result

  def page11(self):
    """GET getAll (requests 1101-1102)."""
    self.token__ = \
      '1295889601547'
    self.token_sort = \
      'title'
    self.token_sortDir = \
      'asc'
    self.token_searchString = \
      ''
    self.token_filterString = \
      '{}'
    result = request1101.GET('/oib/item/manage/getAll' +
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

    grinder.sleep(58)
    request1102.GET('/oib/static/images/manage/standards_bullet_image.png')

    return result

  def page12(self):
    """GET keepalive (request 1201)."""
    self.token__ = \
      '1295889626160'
    result = request1201.GET('/oib/keepalive' +
      '?_=' +
      self.token__)

    return result

  def page13(self):
    """GET standardsTree (request 1301)."""
    self.token__ = \
      '1295889639146'
    self.token_rootId = \
      '33807'
    result = request1301.GET('/oib/standards/item/standardsTree' +
      '?_=' +
      self.token__ +
      '&subject=' +
      self.token_subject +
      '&rootId=' +
      self.token_rootId +
      '&echo=' +
      self.token_echo)

    return result

  def page14(self):
    """GET alignedToSubtree (request 1401)."""
    self.token__ = \
      '1295889639379'
    self.token_nodeId = \
      '33807'
    result = request1401.GET('/oib/item/manage/alignedToSubtree' +
      '?_=' +
      self.token__ +
      '&sort=' +
      self.token_sort +
      '&sortDir=' +
      self.token_sortDir +
      '&nodeId=' +
      self.token_nodeId +
      '&forSelect=' +
      self.token_forSelect +
      '&searchString=' +
      self.token_searchString +
      '&filterString=' +
      self.token_filterString)

    return result

  def page15(self):
    """GET standardsTreeGrandkids (request 1501)."""
    self.token__ = \
      '1295889640605'
    self.token_nodeId = \
      '33808'
    result = request1501.GET('/oib/standards/item/standardsTreeGrandkids' +
      '?_=' +
      self.token__ +
      '&nodeId=' +
      self.token_nodeId +
      '&echo=' +
      self.token_echo)

    return result

  def page16(self):
    """GET alignedToSubtree (request 1601)."""
    self.token__ = \
      '1295889640609'
    result = request1601.GET('/oib/item/manage/alignedToSubtree' +
      '?_=' +
      self.token__ +
      '&sort=' +
      self.token_sort +
      '&sortDir=' +
      self.token_sortDir +
      '&nodeId=' +
      self.token_nodeId +
      '&forSelect=' +
      self.token_forSelect +
      '&searchString=' +
      self.token_searchString +
      '&filterString=' +
      self.token_filterString)

    return result

  def page17(self):
    """GET standardsTreeGrandkids (request 1701)."""
    self.token__ = \
      '1295889646931'
    self.token_nodeId = \
      '33809'
    result = request1701.GET('/oib/standards/item/standardsTreeGrandkids' +
      '?_=' +
      self.token__ +
      '&nodeId=' +
      self.token_nodeId +
      '&echo=' +
      self.token_echo)

    return result

  def page18(self):
    """GET alignedToSubtree (request 1801)."""
    self.token__ = \
      '1295889646937'
    result = request1801.GET('/oib/item/manage/alignedToSubtree' +
      '?_=' +
      self.token__ +
      '&sort=' +
      self.token_sort +
      '&sortDir=' +
      self.token_sortDir +
      '&nodeId=' +
      self.token_nodeId +
      '&forSelect=' +
      self.token_forSelect +
      '&searchString=' +
      self.token_searchString +
      '&filterString=' +
      self.token_filterString)

    return result

  def page19(self):
    """GET standardsTreeGrandkids (request 1901)."""
    self.token__ = \
      '1295889649851'
    self.token_nodeId = \
      '33810'
    result = request1901.GET('/oib/standards/item/standardsTreeGrandkids' +
      '?_=' +
      self.token__ +
      '&nodeId=' +
      self.token_nodeId +
      '&echo=' +
      self.token_echo)

    return result

  def page20(self):
    """GET alignedToSubtree (request 2001)."""
    self.token__ = \
      '1295889649855'
    result = request2001.GET('/oib/item/manage/alignedToSubtree' +
      '?_=' +
      self.token__ +
      '&sort=' +
      self.token_sort +
      '&sortDir=' +
      self.token_sortDir +
      '&nodeId=' +
      self.token_nodeId +
      '&forSelect=' +
      self.token_forSelect +
      '&searchString=' +
      self.token_searchString +
      '&filterString=' +
      self.token_filterString)

    return result

  def page21(self):
    """GET alignedToSubtree (request 2101)."""
    self.token__ = \
      '1295889653029'
    self.token_nodeId = \
      '33811'
    result = request2101.GET('/oib/item/manage/alignedToSubtree' +
      '?_=' +
      self.token__ +
      '&sort=' +
      self.token_sort +
      '&sortDir=' +
      self.token_sortDir +
      '&nodeId=' +
      self.token_nodeId +
      '&forSelect=' +
      self.token_forSelect +
      '&searchString=' +
      self.token_searchString +
      '&filterString=' +
      self.token_filterString)

    return result

  def page22(self):
    """GET alignedToNode (request 2201)."""
    self.token__ = \
      '1295889655085'
    self.token_nodeId = \
      '33812'
    result = request2201.GET('/oib/item/manage/alignedToNode' +
      '?_=' +
      self.token__ +
      '&sort=' +
      self.token_sort +
      '&sortDir=' +
      self.token_sortDir +
      '&nodeId=' +
      self.token_nodeId +
      '&page=' +
      self.token_page +
      '&forSelect=' +
      self.token_forSelect +
      '&searchString=' +
      self.token_searchString +
      '&filterString=' +
      self.token_filterString)

    return result

  def page23(self):
    """POST add (request 2301)."""
    result = request2301.POST('/oib/assessment/component/add',
      ( NVPair('type', 'item'),
        NVPair('subject', 'ELA'),
        NVPair('isEdit', 'false'),
        NVPair('forPassage', 'false'),
        NVPair('vcid', '1179'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page24(self):
    """GET keepalive (requests 2401-2406)."""
    self.token__ = \
      '1295889686161'
    result = request2401.GET('/oib/keepalive' +
      '?_=' +
      self.token__)

    grinder.sleep(16332)
    request2402.GET('/oib/static/images/assessment/rounded_corner_yellow_vert_bg.png')

    request2403.GET('/oib/static/images/assessment/rounded_corner_yellow_top.png')

    grinder.sleep(15)
    request2404.GET('/oib/static/images/assessment/icons_actions.gif')

    request2405.GET('/oib/static/images/assessment/rounded_corner_yellow_horiz_bg.png')

    request2406.GET('/oib/static/images/assessment/rounded_corner_yellow_top_ffffd1.png')

    return result

  def page25(self):
    """POST assessments (request 2501)."""
    result = request2501.POST('/oib/pools/list/assessments',
      ( NVPair('assessmentJSON', '{\"subject\": \"ELA\", \"title\": \"Load test assessment\", \"type\": \"ad_hoc\", \"delivery\": \"offline\", \"body\": {\"main_content\": [{\"type\": \"booklet\", \"title\": \"\", \"children\": [{\"type\": \"item\", \"vcid\": \"1179\", \"version\": \"1\", \"entity_id\": \"841\", \"selectedRubricStandards\": {}, \"standard\": \"33812\"}]}]}}'),
        NVPair('poolId', '831'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page26(self):
    """POST assessments (request 2601)."""
    result = request2601.POST('/oib/pools/list/assessments',
      ( NVPair('assessmentJSON', '{\"subject\": \"ELA\", \"title\": \"Load test assessment\", \"type\": \"ad_hoc\", \"delivery\": \"offline\", \"body\": {\"main_content\": [{\"type\": \"booklet\", \"title\": \"\", \"children\": [{\"type\": \"item\", \"vcid\": \"1179\", \"version\": \"1\", \"entity_id\": \"841\", \"selectedRubricStandards\": {}, \"standard\": \"33812\"}]}]}}'),
        NVPair('poolId', '831'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page27(self):
    """GET manage (requests 2701-2720)."""
    self.token__ = \
      '1295889728132'
    self.token_forAssessment = \
      'true'
    result = request2701.GET('/oib/passage/manage' +
      '?forSelect=' +
      self.token_forSelect +
      '&_=' +
      self.token__ +
      '&subject=' +
      self.token_subject +
      '&forAssessment=' +
      self.token_forAssessment +
      '&isMultiSelect=' +
      self.token_isMultiSelect)

    grinder.sleep(35)
    self.token__ = \
      '1295889728277'
    request2702.GET('/oib/static/js/ViewItemBankEntity.js' +
      '?_=' +
      self.token__)

    grinder.sleep(24)
    self.token__ = \
      '1295889728305'
    request2703.GET('/oib/static/js/widgets/sharing.js' +
      '?_=' +
      self.token__)

    grinder.sleep(14)
    self.token__ = \
      '1295889728321'
    request2704.GET('/oib/static/js/standardsBrowser/createStandardsUi.js' +
      '?_=' +
      self.token__)

    grinder.sleep(146)
    self.token__ = \
      '1295889728469'
    request2705.GET('/oib/static/js/standardsBrowser/viewStandardsUi.js' +
      '?_=' +
      self.token__)

    grinder.sleep(14)
    self.token__ = \
      '1295889728486'
    request2706.GET('/oib/static/js/widgets/tooltip.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728493'
    request2707.GET('/oib/static/js/widgets/AssignmentCreator.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728500'
    request2708.GET('/oib/static/js/EntityPopupSourceUI.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728505'
    request2709.GET('/oib/static/js/manage/ManageBrowser.js' +
      '?_=' +
      self.token__)

    grinder.sleep(20)
    self.token__ = \
      '1295889728531'
    request2710.GET('/oib/static/js/manage/ManageBrowserRenderer.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728537'
    request2711.GET('/oib/static/js/manage/ManagePassageBrowserRenderer.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728543'
    request2712.GET('/oib/static/js/standardsBrowser/ManageStandardsUi.js' +
      '?_=' +
      self.token__)

    grinder.sleep(21)
    self.token__ = \
      '1295889728566'
    request2713.GET('/oib/static/js/manage/AssessmentFilterWidget.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728572'
    request2714.GET('/oib/static/js/manage/ManageFilterWidget.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728579'
    request2715.GET('/oib/static/js/item/question/QuestionType.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728584'
    request2716.GET('/oib/static/js/item/question/OpenResponseQuestionType.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728591'
    request2717.GET('/oib/static/js/widgets/SubjectDropdown.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728596'
    request2718.GET('/oib/static/js/widgets/EditPageSubjectDropdown.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728603'
    request2719.GET('/oib/static/common/js/3p/jqueryMultiSelect.js' +
      '?_=' +
      self.token__)

    self.token__ = \
      '1295889728614'
    request2720.GET('/oib/static/js/manage/manage_ready.js' +
      '?_=' +
      self.token__)

    return result

  def page28(self):
    """GET myStandardsRootNodes (request 2801)."""
    self.token__ = \
      '1295889728686'
    result = request2801.GET('/oib/standards/passage/myStandardsRootNodes' +
      '?_=' +
      self.token__ +
      '&echo=' +
      self.token_echo +
      '&getAlignCount=' +
      self.token_getAlignCount +
      '&subject=' +
      self.token_subject)

    return result

  def page29(self):
    """GET getAll (request 2901)."""
    self.token__ = \
      '1295889728688'
    result = request2901.GET('/oib/passage/manage/getAll' +
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

    return result

  def page30(self):
    """GET keepalive (request 3001)."""
    self.token__ = \
      '1295889746586'
    result = request3001.GET('/oib/keepalive' +
      '?_=' +
      self.token__)

    return result

  def page31(self):
    """GET getAll (request 3101)."""
    self.token__ = \
      '1295889783397'
    self.token_searchString = \
      'body'
    result = request3101.GET('/oib/passage/manage/getAll' +
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

    return result

  def page32(self):
    """GET getAll (request 3201)."""
    self.token__ = \
      '1295889800075'
    self.token_filterString = \
      '{\"pool\":[\"5\"]}'
    result = request3201.GET('/oib/passage/manage/getAll' +
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

    return result

  def page33(self):
    """GET keepalive (request 3301)."""
    self.token__ = \
      '1295889806587'
    result = request3301.GET('/oib/keepalive' +
      '?_=' +
      self.token__)

    return result

  def page34(self):
    """POST add (requests 3401-3403)."""
    result = request3401.POST('/oib/assessment/component/add',
      ( NVPair('type', 'passage'),
        NVPair('subject', 'ELA'),
        NVPair('isEdit', 'false'),
        NVPair('forPassage', 'false'),
        NVPair('vcid', '1310'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    grinder.sleep(8435)
    request3402.GET('/oib/static/images/assessment/rounded_corner_yellow_vert.png')

    request3403.GET('/oib/static/images/assessment/rounded_corner_yellow_horiz.png')

    return result

  def page35(self):
    """POST assessments (requests 3501-3502)."""
    result = request3501.POST('/oib/pools/list/assessments',
      ( NVPair('assessmentJSON', '{\"subject\": \"ELA\", \"title\": \"Load test assessment\", \"type\": \"ad_hoc\", \"delivery\": \"offline\", \"body\": {\"main_content\": [{\"type\": \"booklet\", \"title\": \"\", \"children\": [{\"type\": \"item\", \"vcid\": \"1179\", \"version\": \"1\", \"entity_id\": \"841\", \"selectedRubricStandards\": {}, \"standard\": \"33812\"}, {\"type\": \"passage\", \"vcid\": \"1310\", \"version\": \"1\", \"entity_id\": \"67\", \"children\": [{\"type\": \"item\", \"vcid\": \"1394\", \"version\": \"1\", \"entity_id\": \"1013\", \"selectedRubricStandards\": {\"196\": \"33812\"}}]}]}]}}'),
        NVPair('poolId', '831'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    grinder.sleep(30527)
    request3502.GET('/oib/static/images/sprites/buttons.png')

    return result

  def page36(self):
    """POST studentTest (request 3601)."""
    result = request3601.POST('/oib/assessment/preview/studentTest',
      ( NVPair('assessmentJSON', '{\"subject\": \"ELA\", \"title\": \"Load test assessment\", \"type\": \"ad_hoc\", \"delivery\": \"offline\", \"body\": {\"main_content\": [{\"type\": \"booklet\", \"title\": \"\", \"children\": [{\"type\": \"item\", \"vcid\": \"1179\", \"version\": \"1\", \"entity_id\": \"841\", \"selectedRubricStandards\": {}, \"standard\": \"33812\"}, {\"type\": \"passage\", \"vcid\": \"1310\", \"version\": \"1\", \"entity_id\": \"67\", \"children\": [{\"type\": \"item\", \"vcid\": \"1394\", \"version\": \"1\", \"entity_id\": \"1013\", \"selectedRubricStandards\": {\"196\": \"33812\"}}]}]}]}}'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))

    return result

  def page37(self):
    """GET keepalive (requests 3701-3729)."""
    self.token__ = \
      '1295889866576'
    result = request3701.GET('/oib/keepalive' +
      '?_=' +
      self.token__)

    grinder.sleep(25861)
    request3702.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/langs/en.js')

    request3703.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/editor_template.js')

    request3704.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelveimage/editor_plugin.js')

    request3705.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/advimagescale/editor_plugin.js')

    request3706.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/editor_plugin.js')

    request3707.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/atomic/editor_plugin.js')

    request3708.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/inlinepopups/editor_plugin.js')

    request3709.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/autoresize/editor_plugin.js')

    request3710.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/table/editor_plugin.js')

    request3711.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/paste/editor_plugin.js')

    request3712.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/editor_plugin.js')

    request3713.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/editor_plugin.js')

    grinder.sleep(23)
    request3714.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/langs/en.js')

    grinder.sleep(46)
    request3715.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui.css')

    request3716.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui_threetwelve.css')

    request3717.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/inlinepopups/skins/clearlooks2/window.css')

    grinder.sleep(76)
    request3718.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/img/button_bg.png')

    request3719.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/img/icons.gif')

    request3720.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/img/small.png')

    request3721.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/img/large.png')

    request3722.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/img/medium.png')

    request3723.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/img/ed_mathformula.gif')

    request3724.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_space_title_2.gif')

    request3725.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_space_title_1.gif')

    request3726.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_space_title_3.gif')

    request3727.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_add_space_ruled.png')

    request3728.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_add_space_unruled.png')

    grinder.sleep(20)
    request3729.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/content.css')

    return result

  def page38(self):
    """POST add (request 3801)."""
    result = request3801.POST('/oib/assessment/component/add',
      ( NVPair('type', 'instruction'),
        NVPair('subject', 'ELA'),
        NVPair('isEdit', 'false'),
        NVPair('forPassage', 'true'),
        NVPair('addedPassages', '1310'),
        NVPair('text', '<p>Load test assessment directions</p>'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page39(self):
    """GET keepalive (request 3901)."""
    self.token__ = \
      '1295889926586'
    result = request3901.GET('/oib/keepalive' +
      '?_=' +
      self.token__)

    return result

  def page40(self):
    """POST add (request 4001)."""
    result = request4001.POST('/oib/assessment/component/add',
      ( NVPair('type', 'proctor_instruction'),
        NVPair('subject', 'ELA'),
        NVPair('isEdit', 'false'),
        NVPair('forPassage', 'true'),
        NVPair('addedPassages', '1310'),
        NVPair('text', '<p>Load test assessment proctor directions</p>'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page41(self):
    """POST add (requests 4101-4102)."""
    result = request4101.POST('/oib/assessment/component/add',
      ( NVPair('type', 'page_break'),
        NVPair('subject', 'ELA'),
        NVPair('isEdit', 'false'),
        NVPair('forPassage', 'false'),
        NVPair('addedPassages', '1310'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    request4102.GET('/oib/static/images/assessment/icon_page_break.png')

    return result

  def page42(self):
    """POST add (requests 4201-4202)."""
    result = request4201.POST('/oib/assessment/component/add',
      ( NVPair('type', 'stop'),
        NVPair('subject', 'ELA'),
        NVPair('isEdit', 'false'),
        NVPair('forPassage', 'false'),
        NVPair('addedPassages', '1310'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    grinder.sleep(17)
    request4202.GET('/oib/static/images/assessment/icon_stop.png')

    return result

  def page43(self):
    """GET keepalive (requests 4301-4302)."""
    self.token__ = \
      '1295889986587'
    result = request4301.GET('/oib/keepalive' +
      '?_=' +
      self.token__)

    grinder.sleep(18846)
    request4302.GET('/oib/static/images/assessment/button_save_preview_90dcfc.png')

    return result

  def page44(self):
    """GET keepalive (request 4401)."""
    self.token__ = \
      '1295890046586'
    result = request4401.GET('/oib/keepalive' +
      '?_=' +
      self.token__)

    return result

  def page45(self):
    """POST sharingAgreement (request 4501)."""
    result = request4501.POST('/oib/sharingAgreement',
      '',
      ( NVPair('Content-Type', 'text/plain; charset=UTF-8'), ))

    return result

  def page46(self):
    """POST save (requests 4601-4604)."""
    result = request4601.POST('/oib/assessment/save',
      ( NVPair('assessmentJSON', '{\"subject\": \"ELA\", \"title\": \"Load test assessment\", \"type\": \"ad_hoc\", \"delivery\": \"offline\", \"body\": {\"main_content\": [{\"type\": \"booklet\", \"title\": \"\", \"children\": [{\"type\": \"item\", \"vcid\": \"1179\", \"version\": \"1\", \"entity_id\": \"841\", \"selectedRubricStandards\": {}, \"standard\": \"33812\"}, {\"type\": \"stop\"}, {\"type\": \"passage\", \"vcid\": \"1310\", \"version\": \"1\", \"entity_id\": \"67\", \"children\": [{\"type\": \"item\", \"vcid\": \"1394\", \"version\": \"1\", \"entity_id\": \"1013\", \"selectedRubricStandards\": {\"196\": \"33812\"}}, {\"type\": \"instruction\", \"body\": \"\\n            <div class=\\\"styledTextMarker\\\"></div><p>Load test assessment directions</p>\\n      \"}, {\"type\": \"proctor_instruction\", \"body\": \"\\n            <div class=\\\"styledTextMarker\\\"></div><p>Load test assessment proctor directions</p>\\n      \"}]}, {\"type\": \"page_break\"}]}]}}'),
        NVPair('subject', 'ELA'),
        NVPair('ctoken', 'DlYggFsV'),
        NVPair('poolId', '831'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    grinder.sleep(24)
    request4602.GET('/oib/static/images/connectors/create_box_top.png')

    request4603.GET('/oib/static/images/connectors/create_box_bkgrd.png')

    request4604.GET('/oib/static/images/connectors/create_box_bottom.png')

    return result

  def page47(self):
    """GET create (request 4701)."""
    self.token_id = \
      '1395'
    result = request4701.GET('/oib/assessment/create' +
      '?id=' +
      self.token_id)

    return result

  def page48(self):
    """POST assessments (request 4801)."""
    result = request4801.POST('/oib/pools/list/assessments',
      ( NVPair('assessmentId', '74'),
        NVPair('poolId', '831'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page49(self):
    """GET home (requests 4901-4902)."""
    result = request4901.GET('/oib/home')

    grinder.sleep(97)
    request4902.GET('/oib/static/images/dashboard/video_box_gradient.png')

    return result

  def page50(self):
    """GET recent (requests 5001-5003)."""
    self.token__ = \
      '1295890112666'
    result = request5001.GET('/oib/webservices/entities/recent' +
      '?type=' +
      self.token_type +
      '&pageSize=' +
      self.token_pageSize +
      '&page=' +
      self.token_page +
      '&_=' +
      self.token__)

    grinder.sleep(272)
    request5002.GET('/oib/static/images/view_overlay/sprites.png')

    request5003.GET('/oib/static/images/manage/assessment_item_count_box.png')

    return result

  def page51(self):
    """GET logout (requests 5101-5102)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request5101.GET('/oib/logout')

    request5102.GET('/wgen/Logout.do')

    return result

  def getFirstItemIds(self, result):
    resultString = result.text.replace(r"\'", "'") # Jyson doesn't like escaped apostrophes.
    resultJSON = json.loads(resultString)
    itemIds = {}
    if 'ap' in resultJSON:
      itemNode = resultJSON['ap']['itemlist'][0]['subpageItems']['itemlist'][0]
      itemIds['vcid'] = itemNode['vcid']
      itemIds['entity_id'] = itemNode['entity_id']
      itemIds['versionNum'] = itemNode['versionNum']
      if 'asId' in resultJSON['ap']['itemlist'][0]:
        itemIds['asID'] = resultJSON['ap']['itemlist'][0]['asID']
    elif 'it' in resultJSON:
      itemNode = resultJSON['it']['itemlist'][0]
      itemIds['vcid'] = itemNode['vcid']
      itemIds['entity_id'] = itemNode['entity_id']
      itemIds['versionNum'] = itemNode['versionNum']
      if 'standardInfo' in resultJSON:
        itemIds['asID'] = resultJSON['standardInfo']['asID']
    else:
      raise LookupError("Cannot parse ids from result: %s" % resultString)
    return itemIds

  def __call__(self):
    """This method is called for every run performed by the worker thread."""
    self.page1()      # GET login (requests 101-102)

    # grinder.sleep(3467)
    self.page2()      # POST login (requests 201-266)

    # grinder.sleep(204)
    self.page3()      # GET ga.js (request 301)

    # grinder.sleep(149)
    self.page4()      # GET recent (request 401)
    self.page5()      # GET ellipsis.xml (requests 501-502)

    # grinder.sleep(12165)
    self.page6()      # GET create (requests 601-604)
    self.page7()      # GET empty.html (requests 701-726)

    # grinder.sleep(35601)
    self.page8()      # POST assessments (requests 801-803)
    self.page9()      # GET manage (requests 901-926)

    # grinder.sleep(70)
    self.page10()     # GET myStandardsRootNodes (request 1001)
    self.page11()     # GET getAll (requests 1101-1102)

    # grinder.sleep(21318)
    self.page12()     # GET keepalive (request 1201)

    # grinder.sleep(12961)
    self.page13()     # GET standardsTree (request 1301)

    # grinder.sleep(67)
    result = self.page14()     # GET alignedToSubtree (request 1401)
    self.page15()     # GET standardsTreeGrandkids (request 1501)
    self.page16()     # GET alignedToSubtree (request 1601)

    # grinder.sleep(4693)
    self.page17()     # GET standardsTreeGrandkids (request 1701)
    self.page18()     # GET alignedToSubtree (request 1801)

    # grinder.sleep(2484)
    self.page19()     # GET standardsTreeGrandkids (request 1901)
    self.page20()     # GET alignedToSubtree (request 2001)

    # grinder.sleep(2671)
    self.page21()     # GET alignedToSubtree (request 2101)

    # grinder.sleep(1877)
    result = self.page22()     # GET alignedToNode (request 2201)
    item_ids = self.getFirstItemIds(result)

    # grinder.sleep(25510)
    self.page23()     # POST add (request 2301)

    # grinder.sleep(5241)
    self.page24()     # GET keepalive (requests 2401-2406)
    self.page25()     # POST assessments (request 2501)

    # grinder.sleep(25408)
    self.page26()     # POST assessments (request 2601)
    self.page27()     # GET manage (requests 2701-2720)

    # grinder.sleep(70)
    self.page28()     # GET myStandardsRootNodes (request 2801)
    self.page29()     # GET getAll (request 2901)

    # grinder.sleep(16585)
    self.page30()     # GET keepalive (request 3001)

    # grinder.sleep(36748)
    self.page31()     # GET getAll (request 3101)

    # grinder.sleep(15524)
    result = self.page32()     # GET getAll (request 3201)
    passage_ids = self.getFirstItemIds(result)

    # grinder.sleep(5511)
    self.page33()     # GET keepalive (request 3301)

    # grinder.sleep(8937)
    self.page34()     # POST add (requests 3401-3403)
    self.page35()     # POST assessments (requests 3501-3502)

    # grinder.sleep(9068)
    self.page36()     # POST studentTest (request 3601)

    # grinder.sleep(2239)
    self.page37()     # GET keepalive (requests 3701-3729)

    # grinder.sleep(31615)
    self.page38()     # POST add (request 3801)

    # grinder.sleep(2156)
    self.page39()     # GET keepalive (request 3901)

    # grinder.sleep(32218)
    self.page40()     # POST add (request 4001)

    # grinder.sleep(16614)
    self.page41()     # POST add (requests 4101-4102)

    # grinder.sleep(5948)
    self.page42()     # POST add (requests 4201-4202)

    # grinder.sleep(4961)
    self.page43()     # GET keepalive (requests 4301-4302)

    # grinder.sleep(41123)
    self.page44()     # GET keepalive (request 4401)

    # grinder.sleep(26084)
    self.page45()     # POST sharingAgreement (request 4501)

    # grinder.sleep(12751)
    self.page46()     # POST save (requests 4601-4604)

    # grinder.sleep(14616)
    self.page47()     # GET create (request 4701)

    # grinder.sleep(739)
    self.page48()     # POST assessments (request 4801)

    # grinder.sleep(9871)
    self.page49()     # GET home (requests 4901-4902)

    # grinder.sleep(319)
    self.page50()     # GET recent (requests 5001-5003)

    # grinder.sleep(3031)
    self.page51()     # GET logout (requests 5101-5102)

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
