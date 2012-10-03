# The Grinder 3.4
# HTTP script recorded by TCPProxy at Jan 24, 2011 11:34:44 AM

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
    NVPair('Referer', 'http://localhost:8000/oib/home;jsessionid=B9DAE0430B7D8E7B413D0B35068EF0F8'), ]

headers4= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/home;jsessionid=B9DAE0430B7D8E7B413D0B35068EF0F8'), ]

headers5= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://localhost:8000/oib/home;jsessionid=B9DAE0430B7D8E7B413D0B35068EF0F8'), ]

headers6= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/common/css/widgets/mClassNavBar.css'), ]

headers7= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/common/css/basic.css'), ]

headers8= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/common/css/widgets/GlobalNavBar.css'), ]

headers9= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/common/css/skin.css'), ]

headers10= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/dashboard.css'), ]

headers11= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'http://localhost:8000/oib/home;jsessionid=B9DAE0430B7D8E7B413D0B35068EF0F8'), ]

headers12= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/manage/manage_passage.css'), ]

headers13= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/manage/manage_assessment.css'), ]

headers14= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8000/oib/home;jsessionid=B9DAE0430B7D8E7B413D0B35068EF0F8'), ]

headers15= \
  [ NVPair('Accept', 'text/css,*/*;q=0.1'),
    NVPair('Referer', 'http://localhost:8000/oib/passage/create?fromManage=false'), ]

headers16= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/passage/create?fromManage=false'), ]

headers17= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8000/oib/passage/create?fromManage=false'), ]

headers18= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/common/css/3p/jqueryMultiSelect.css'), ]

headers19= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://localhost:8000/oib/passage/create?fromManage=false'), ]

headers20= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/css/jquery-ui-1.7.2.custom.css'), ]

headers21= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui.css'), ]

headers22= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://localhost:8000/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui_threetwelve.css'), ]

headers23= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://localhost:8000/oib/passage/create?fromManage=false'),
    NVPair('Cache-Control', 'no-cache'), ]

headers25= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://localhost:8000/oib/passage/create?fromManage=false&id=1392'), ]

headers26= \
  [ NVPair('Accept', 'application/json, text/javascript, */*'),
    NVPair('Referer', 'http://localhost:8000/oib/home'), ]

headers27= \
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
request204 = Test(204, 'GET GlobalNavBar.css').wrap(request204)

request205 = HTTPRequest(url=url0, headers=headers3)
request205 = Test(205, 'GET styled_text.css').wrap(request205)

request206 = HTTPRequest(url=url0, headers=headers4)
request206 = Test(206, 'GET logo_mclass_navbar.gif').wrap(request206)

request207 = HTTPRequest(url=url0, headers=headers3)
request207 = Test(207, 'GET skin.css').wrap(request207)

request208 = HTTPRequest(url=url0, headers=headers3)
request208 = Test(208, 'GET jquery-ui-1.7.2.custom.css').wrap(request208)

request209 = HTTPRequest(url=url0, headers=headers3)
request209 = Test(209, 'GET help.css').wrap(request209)

request210 = HTTPRequest(url=url0, headers=headers3)
request210 = Test(210, 'GET mClassNavBar.css').wrap(request210)

request211 = HTTPRequest(url=url0, headers=headers3)
request211 = Test(211, 'GET standards.css').wrap(request211)

request212 = HTTPRequest(url=url0, headers=headers3)
request212 = Test(212, 'GET dashboard.css').wrap(request212)

request213 = HTTPRequest(url=url0, headers=headers3)
request213 = Test(213, 'GET manage.css').wrap(request213)

request214 = HTTPRequest(url=url0, headers=headers3)
request214 = Test(214, 'GET manage_passage.css').wrap(request214)

request215 = HTTPRequest(url=url0, headers=headers3)
request215 = Test(215, 'GET manage_rubric.css').wrap(request215)

request216 = HTTPRequest(url=url0, headers=headers3)
request216 = Test(216, 'GET manage_assessment.css').wrap(request216)

request217 = HTTPRequest(url=url0, headers=headers3)
request217 = Test(217, 'GET manage_item.css').wrap(request217)

request218 = HTTPRequest(url=url0, headers=headers3)
request218 = Test(218, 'GET view_entity.css').wrap(request218)

request219 = HTTPRequest(url=url0, headers=headers3)
request219 = Test(219, 'GET jqueryMultiSelect.css').wrap(request219)

request220 = HTTPRequest(url=url0, headers=headers5)
request220 = Test(220, 'GET closure.base.js').wrap(request220)

request221 = HTTPRequest(url=url0, headers=headers4)
request221 = Test(221, 'GET px.gif').wrap(request221)

request222 = HTTPRequest(url=url0, headers=headers5)
request222 = Test(222, 'GET ui.core.js').wrap(request222)

request223 = HTTPRequest(url=url0, headers=headers5)
request223 = Test(223, 'GET ui.draggable.js').wrap(request223)

request224 = HTTPRequest(url=url0, headers=headers5)
request224 = Test(224, 'GET jquery-1.3.2.js').wrap(request224)

request225 = HTTPRequest(url=url0, headers=headers5)
request225 = Test(225, 'GET ui.sortable.js').wrap(request225)

request226 = HTTPRequest(url=url0, headers=headers5)
request226 = Test(226, 'GET ui.resizable.js').wrap(request226)

request227 = HTTPRequest(url=url0, headers=headers5)
request227 = Test(227, 'GET ui.slider.js').wrap(request227)

request228 = HTTPRequest(url=url0, headers=headers5)
request228 = Test(228, 'GET ui.dialog.js').wrap(request228)

request229 = HTTPRequest(url=url0, headers=headers5)
request229 = Test(229, 'GET jquery_setup.js').wrap(request229)

request230 = HTTPRequest(url=url0, headers=headers5)
request230 = Test(230, 'GET jquery.form.js').wrap(request230)

request231 = HTTPRequest(url=url0, headers=headers5)
request231 = Test(231, 'GET jsonStringify.js').wrap(request231)

request232 = HTTPRequest(url=url0, headers=headers5)
request232 = Test(232, 'GET prototype.js').wrap(request232)

request233 = HTTPRequest(url=url0, headers=headers5)
request233 = Test(233, 'GET ui.tabs.js').wrap(request233)

request234 = HTTPRequest(url=url0, headers=headers5)
request234 = Test(234, 'GET autoresize.jquery.min.js').wrap(request234)

request235 = HTTPRequest(url=url0, headers=headers5)
request235 = Test(235, 'GET jquery.tooltip.js').wrap(request235)

request236 = HTTPRequest(url=url0, headers=headers5)
request236 = Test(236, 'GET standards.js').wrap(request236)

request237 = HTTPRequest(url=url0, headers=headers5)
request237 = Test(237, 'GET BackspaceSuppress.js').wrap(request237)

request238 = HTTPRequest(url=url0, headers=headers5)
request238 = Test(238, 'GET math-utilities.js').wrap(request238)

request239 = HTTPRequest(url=url0, headers=headers5)
request239 = Test(239, 'GET standardsUi.js').wrap(request239)

request240 = HTTPRequest(url=url0, headers=headers5)
request240 = Test(240, 'GET LaTeXMathML.js').wrap(request240)

request241 = HTTPRequest(url=url0, headers=headers5)
request241 = Test(241, 'GET TimeoutDetect.js').wrap(request241)

request242 = HTTPRequest(url=url0, headers=headers5)
request242 = Test(242, 'GET wgen.oib.utilities.js').wrap(request242)

request243 = HTTPRequest(url=url0, headers=headers5)
request243 = Test(243, 'GET RoboHelp_CSH.js').wrap(request243)

request244 = HTTPRequest(url=url0, headers=headers5)
request244 = Test(244, 'GET global_ready.js').wrap(request244)

request245 = HTTPRequest(url=url0, headers=headers5)
request245 = Test(245, 'GET jquery_functions.js').wrap(request245)

request246 = HTTPRequest(url=url0, headers=headers5)
request246 = Test(246, 'GET help.js').wrap(request246)

request247 = HTTPRequest(url=url0, headers=headers5)
request247 = Test(247, 'GET cookieHandler.js').wrap(request247)

request248 = HTTPRequest(url=url0, headers=headers5)
request248 = Test(248, 'GET ViewItemBankEntity.js').wrap(request248)

request249 = HTTPRequest(url=url0, headers=headers5)
request249 = Test(249, 'GET SharingDropdown.js').wrap(request249)

request250 = HTTPRequest(url=url0, headers=headers5)
request250 = Test(250, 'GET EntityPopupSourceUI.js').wrap(request250)

request251 = HTTPRequest(url=url0, headers=headers5)
request251 = Test(251, 'GET jqueryMultiSelect.js').wrap(request251)

request252 = HTTPRequest(url=url0, headers=headers5)
request252 = Test(252, 'GET ManageBrowserRenderer.js').wrap(request252)

request253 = HTTPRequest(url=url0, headers=headers5)
request253 = Test(253, 'GET googleAnalytics.js').wrap(request253)

request254 = HTTPRequest(url=url0, headers=headers5)
request254 = Test(254, 'GET tooltip.js').wrap(request254)

request255 = HTTPRequest(url=url0, headers=headers5)
request255 = Test(255, 'GET ManageItemBrowserRenderer.js').wrap(request255)

request256 = HTTPRequest(url=url0, headers=headers5)
request256 = Test(256, 'GET viewStandardsUi.js').wrap(request256)

request257 = HTTPRequest(url=url0, headers=headers5)
request257 = Test(257, 'GET ManagePassageBrowserRenderer.js').wrap(request257)

request258 = HTTPRequest(url=url0, headers=headers5)
request258 = Test(258, 'GET sharing.js').wrap(request258)

request259 = HTTPRequest(url=url0, headers=headers5)
request259 = Test(259, 'GET createStandardsUi.js').wrap(request259)

request260 = HTTPRequest(url=url0, headers=headers5)
request260 = Test(260, 'GET ManageBrowser.js').wrap(request260)

request261 = HTTPRequest(url=url0, headers=headers4)
request261 = Test(261, 'GET icon_question_contextual.gif').wrap(request261)

request262 = HTTPRequest(url=url0, headers=headers4)
request262 = Test(262, 'GET navbar_logo.gif').wrap(request262)

request263 = HTTPRequest(url=url0, headers=headers6)
request263 = Test(263, 'GET bg_header_blue_dot.gif').wrap(request263)

request264 = HTTPRequest(url=url0, headers=headers7)
request264 = Test(264, 'GET top_bar_divider.gif').wrap(request264)

request265 = HTTPRequest(url=url0, headers=headers8)
request265 = Test(265, 'GET navigation_buttons_sprite.png').wrap(request265)

request266 = HTTPRequest(url=url0, headers=headers8)
request266 = Test(266, 'GET navigation_buttons_icons_sprite.png').wrap(request266)

request267 = HTTPRequest(url=url0, headers=headers9)
request267 = Test(267, 'GET assess_back.png').wrap(request267)

request268 = HTTPRequest(url=url0, headers=headers10)
request268 = Test(268, 'GET video_box_gradient.png').wrap(request268)

request269 = HTTPRequest(url=url0, headers=headers7)
request269 = Test(269, 'GET table_contents_right_tile.gif').wrap(request269)

request270 = HTTPRequest(url=url0, headers=headers7)
request270 = Test(270, 'GET table_contents_corners_sprite.gif').wrap(request270)

request271 = HTTPRequest(url=url0, headers=headers7)
request271 = Test(271, 'GET table_contents_bottom_tile.gif').wrap(request271)

request272 = HTTPRequest(url=url0, headers=headers7)
request272 = Test(272, 'GET ajax-loader-lrg.gif').wrap(request272)

request273 = HTTPRequest(url=url0, headers=headers9)
request273 = Test(273, 'GET body_content_area_corner_sprite.png').wrap(request273)

request274 = HTTPRequest(url=url0, headers=headers5)
request274 = Test(274, 'GET ManageRubricBrowserRenderer.js').wrap(request274)

request275 = HTTPRequest(url=url0, headers=headers5)
request275 = Test(275, 'GET ManageAssessmentBrowserRenderer.js').wrap(request275)

request276 = HTTPRequest(url=url0, headers=headers5)
request276 = Test(276, 'GET RecentEntityWidget.js').wrap(request276)

request277 = HTTPRequest(url=url0, headers=headers5)
request277 = Test(277, 'GET dashboard_ready.js').wrap(request277)

request278 = HTTPRequest(url=url0, headers=headers5)
request278 = Test(278, 'GET DashboardPage.js').wrap(request278)

request279 = HTTPRequest(url=url0, headers=headers5)
request279 = Test(279, 'GET QuestionType.js').wrap(request279)

request280 = HTTPRequest(url=url0, headers=headers5)
request280 = Test(280, 'GET OpenResponseQuestionType.js').wrap(request280)

request281 = HTTPRequest(url=url0, headers=headers5)
request281 = Test(281, 'GET GlobalNavBar.js').wrap(request281)

request301 = HTTPRequest(url=url1, headers=headers5)
request301 = Test(301, 'GET ga.js').wrap(request301)

request401 = HTTPRequest(url=url0, headers=headers11)
request401 = Test(401, 'GET recent').wrap(request401)

request402 = HTTPRequest(url=url0, headers=headers7)
request402 = Test(402, 'GET blue_button_flat.gif').wrap(request402)

request501 = HTTPRequest(url=url0, headers=headers0)
request501 = Test(501, 'GET ellipsis.xml').wrap(request501)

request502 = HTTPRequest(url=url0, headers=headers12)
request502 = Test(502, 'GET locate_rounded_corner_objects.png').wrap(request502)

request503 = HTTPRequest(url=url0, headers=headers13)
request503 = Test(503, 'GET sprites.png').wrap(request503)

request504 = HTTPRequest(url=url0, headers=headers13)
request504 = Test(504, 'GET assessment_item_count_box.png').wrap(request504)

# Passages > Create Passage
request601 = HTTPRequest(url=url0, headers=headers14)
request601 = Test(601, 'GET create').wrap(request601)

request602 = HTTPRequest(url=url0, headers=headers15)
request602 = Test(602, 'GET create.css').wrap(request602)

request603 = HTTPRequest(url=url0, headers=headers16)
request603 = Test(603, 'GET tooltip_win_arrow_top.png').wrap(request603)

request701 = HTTPRequest(url=url0, headers=headers17)
request701 = Test(701, 'GET empty.html').wrap(request701)

request702 = HTTPRequest(url=url0, headers=headers18)
request702 = Test(702, 'GET dropdown_top_bottom_sprite.png').wrap(request702)

request703 = HTTPRequest(url=url0, headers=headers18)
request703 = Test(703, 'GET dropdown_sides.png').wrap(request703)

request704 = HTTPRequest(url=url0, headers=headers7)
request704 = Test(704, 'GET create_box_bottom_connector.png').wrap(request704)

request705 = HTTPRequest(url=url0, headers=headers7)
request705 = Test(705, 'GET create_box_top_connector.png').wrap(request705)

request706 = HTTPRequest(url=url0, headers=headers7)
request706 = Test(706, 'GET slider_sprite.png').wrap(request706)

request707 = HTTPRequest(url=url0, headers=headers7)
request707 = Test(707, 'GET create_box_bottom.png').wrap(request707)

request708 = HTTPRequest(url=url0, headers=headers7)
request708 = Test(708, 'GET create_box_bkgrd.png').wrap(request708)

request709 = HTTPRequest(url=url0, headers=headers7)
request709 = Test(709, 'GET create_box_top.png').wrap(request709)

request710 = HTTPRequest(url=url0, headers=headers19)
request710 = Test(710, 'GET tiny_mce.js').wrap(request710)

request711 = HTTPRequest(url=url0, headers=headers19)
request711 = Test(711, 'GET threetwelveImage.js').wrap(request711)

request712 = HTTPRequest(url=url0, headers=headers19)
request712 = Test(712, 'GET SubjectDropdown.js').wrap(request712)

request713 = HTTPRequest(url=url0, headers=headers19)
request713 = Test(713, 'GET EditPageSubjectDropdown.js').wrap(request713)

request714 = HTTPRequest(url=url0, headers=headers19)
request714 = Test(714, 'GET tooltip.js').wrap(request714)

request715 = HTTPRequest(url=url0, headers=headers19)
request715 = Test(715, 'GET Ajax.js').wrap(request715)

request716 = HTTPRequest(url=url0, headers=headers19)
request716 = Test(716, 'GET EditPage.js').wrap(request716)

request717 = HTTPRequest(url=url0, headers=headers19)
request717 = Test(717, 'GET StyledTextEditor.js').wrap(request717)

request718 = HTTPRequest(url=url0, headers=headers19)
request718 = Test(718, 'GET TimeSlider.js').wrap(request718)

request719 = HTTPRequest(url=url0, headers=headers19)
request719 = Test(719, 'GET GradeRangeSlider.js').wrap(request719)

request720 = HTTPRequest(url=url0, headers=headers19)
request720 = Test(720, 'GET collapsible_panel.js').wrap(request720)

request721 = HTTPRequest(url=url0, headers=headers19)
request721 = Test(721, 'GET Passage.js').wrap(request721)

request722 = HTTPRequest(url=url0, headers=headers19)
request722 = Test(722, 'GET dialog.js').wrap(request722)

request723 = HTTPRequest(url=url0, headers=headers19)
request723 = Test(723, 'GET EditReady.js').wrap(request723)

request724 = HTTPRequest(url=url0, headers=headers20)
request724 = Test(724, 'GET slider.png').wrap(request724)

request725 = HTTPRequest(url=url0, headers=headers16)
request725 = Test(725, 'GET btn_section_expander_item_closed.png').wrap(request725)

request726 = HTTPRequest(url=url0, headers=headers16)
request726 = Test(726, 'GET btn_section_expander_item.png').wrap(request726)

# Fill out Create Passage page and click Preview.
request727 = HTTPRequest(url=url0, headers=headers19)
request727 = Test(727, 'GET en.js').wrap(request727)

request728 = HTTPRequest(url=url0, headers=headers19)
request728 = Test(728, 'GET editor_template.js').wrap(request728)

request729 = HTTPRequest(url=url0, headers=headers19)
request729 = Test(729, 'GET editor_plugin.js').wrap(request729)

request730 = HTTPRequest(url=url0, headers=headers19)
request730 = Test(730, 'GET editor_plugin.js').wrap(request730)

request731 = HTTPRequest(url=url0, headers=headers19)
request731 = Test(731, 'GET editor_plugin.js').wrap(request731)

request732 = HTTPRequest(url=url0, headers=headers19)
request732 = Test(732, 'GET editor_plugin.js').wrap(request732)

request733 = HTTPRequest(url=url0, headers=headers19)
request733 = Test(733, 'GET editor_plugin.js').wrap(request733)

request734 = HTTPRequest(url=url0, headers=headers19)
request734 = Test(734, 'GET editor_plugin.js').wrap(request734)

request735 = HTTPRequest(url=url0, headers=headers19)
request735 = Test(735, 'GET editor_plugin.js').wrap(request735)

request736 = HTTPRequest(url=url0, headers=headers19)
request736 = Test(736, 'GET editor_plugin.js').wrap(request736)

request737 = HTTPRequest(url=url0, headers=headers19)
request737 = Test(737, 'GET editor_plugin.js').wrap(request737)

request738 = HTTPRequest(url=url0, headers=headers19)
request738 = Test(738, 'GET en.js').wrap(request738)

request739 = HTTPRequest(url=url0, headers=headers19)
request739 = Test(739, 'GET editor_plugin.js').wrap(request739)

request740 = HTTPRequest(url=url0, headers=headers15)
request740 = Test(740, 'GET ui.css').wrap(request740)

request741 = HTTPRequest(url=url0, headers=headers15)
request741 = Test(741, 'GET ui_threetwelve.css').wrap(request741)

request742 = HTTPRequest(url=url0, headers=headers15)
request742 = Test(742, 'GET window.css').wrap(request742)

request743 = HTTPRequest(url=url0, headers=headers21)
request743 = Test(743, 'GET button_bg.png').wrap(request743)

request744 = HTTPRequest(url=url0, headers=headers21)
request744 = Test(744, 'GET icons.gif').wrap(request744)

request745 = HTTPRequest(url=url0, headers=headers22)
request745 = Test(745, 'GET small.png').wrap(request745)

request746 = HTTPRequest(url=url0, headers=headers22)
request746 = Test(746, 'GET medium.png').wrap(request746)

request747 = HTTPRequest(url=url0, headers=headers22)
request747 = Test(747, 'GET large.png').wrap(request747)

request748 = HTTPRequest(url=url0, headers=headers22)
request748 = Test(748, 'GET ed_mathformula.gif').wrap(request748)

request749 = HTTPRequest(url=url0, headers=headers22)
request749 = Test(749, 'GET btn_wysiwyg_space_title_2.gif').wrap(request749)

request750 = HTTPRequest(url=url0, headers=headers22)
request750 = Test(750, 'GET btn_wysiwyg_space_title_1.gif').wrap(request750)

request751 = HTTPRequest(url=url0, headers=headers22)
request751 = Test(751, 'GET btn_wysiwyg_space_title_3.gif').wrap(request751)

request752 = HTTPRequest(url=url0, headers=headers22)
request752 = Test(752, 'GET btn_wysiwyg_add_space_ruled.png').wrap(request752)

request753 = HTTPRequest(url=url0, headers=headers22)
request753 = Test(753, 'GET btn_wysiwyg_add_space_unruled.png').wrap(request753)

request754 = HTTPRequest(url=url0, headers=headers15)
request754 = Test(754, 'GET content.css').wrap(request754)

request755 = HTTPRequest(url=url0, headers=headers20)
request755 = Test(755, 'GET border.png').wrap(request755)

request756 = HTTPRequest(url=url0, headers=headers20)
request756 = Test(756, 'GET close_X.png').wrap(request756)

request757 = HTTPRequest(url=url0, headers=headers20)
request757 = Test(757, 'GET buttons.png').wrap(request757)

request801 = HTTPRequest(url=url0, headers=headers23)
request801 = Test(801, 'POST previewPassage').wrap(request801)

request901 = HTTPRequest(url=url0, headers=headers19)
request901 = Test(901, 'GET keepalive').wrap(request901)

# Close preview overlay.
# Select municipality pool.
# Click Save.
request1001 = HTTPRequest(url=url0, headers=headers23)
request1001 = Test(1001, 'POST sharingAgreement').wrap(request1001)

# Click "I Agree".

# Click "Edit Passage".
request1201 = HTTPRequest(url=url0, headers=headers17)
request1201 = Test(1201, 'GET create').wrap(request1201)

# Click "Cancel".
request1301 = HTTPRequest(url=url0, headers=headers25)
request1301 = Test(1301, 'GET home').wrap(request1301)

request1401 = HTTPRequest(url=url0, headers=headers26)
request1401 = Test(1401, 'GET recent').wrap(request1401)

# Log out.
request1501 = HTTPRequest(url=url0, headers=headers27)
request1501 = Test(1501, 'GET logout').wrap(request1501)

request1502 = HTTPRequest(url=url0, headers=headers27)
request1502 = Test(1502, 'GET Logout.do').wrap(request1502)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET login (requests 101-102)."""
    result = request101.GET('/oib/login')

    grinder.sleep(32)
    request102.GET('/oib/static/images/three2twelve.png')

    return result

  def page2(self):
    """POST login (requests 201-281)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request201.POST('/oib/login',
      ( NVPair('username', 'demoCA100105'),
        NVPair('password', ''), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded'), ))
    self.token_jsessionid = \
      httpUtilities.valueFromLocationURI('jsessionid') # 'B9DAE0430B7D8E7B413D0B35068EF0F8'

    grinder.sleep(34)
    request202.GET('/oib/home;jsessionid=' +
      self.token_jsessionid)

    grinder.sleep(23)
    request203.GET('/oib/static/common/css/basic.css')

    request204.GET('/oib/static/common/css/widgets/GlobalNavBar.css')

    request205.GET('/oib/static/css/styled_text.css')

    request206.GET('/oib/static/common/images/mclass/logo_mclass_navbar.gif')

    request207.GET('/oib/static/common/css/skin.css')

    request208.GET('/oib/static/css/jquery-ui-1.7.2.custom.css')

    request209.GET('/oib/static/css/widgets/help.css')

    request210.GET('/oib/static/common/css/widgets/mClassNavBar.css')

    request211.GET('/oib/static/css/standards.css')

    request212.GET('/oib/static/css/dashboard.css')

    request213.GET('/oib/static/css/manage/manage.css')

    request214.GET('/oib/static/css/manage/manage_passage.css')

    request215.GET('/oib/static/css/manage/manage_rubric.css')

    request216.GET('/oib/static/css/manage/manage_assessment.css')

    request217.GET('/oib/static/css/manage/manage_item.css')

    request218.GET('/oib/static/css/view_entity.css')

    request219.GET('/oib/static/common/css/3p/jqueryMultiSelect.css')

    request220.GET('/oib/static/common/js/3p/closure.base.js')

    grinder.sleep(16)
    request221.GET('/oib/static/common/images/mclass/px.gif')

    request222.GET('/oib/static/common/js/3p/jqueryui/ui.core.js')

    request223.GET('/oib/static/common/js/3p/jqueryui/ui.draggable.js')

    request224.GET('/oib/static/common/js/3p/jquery-1.3.2.js')

    request225.GET('/oib/static/common/js/3p/jqueryui/ui.sortable.js')

    request226.GET('/oib/static/common/js/3p/jqueryui/ui.resizable.js')

    request227.GET('/oib/static/common/js/3p/jqueryui/ui.slider.js')

    request228.GET('/oib/static/common/js/3p/jqueryui/ui.dialog.js')

    request229.GET('/oib/static/common/js/jquery_setup.js')

    request230.GET('/oib/static/common/js/3p/jquery.form.js')

    request231.GET('/oib/static/common/js/3p/jsonStringify.js')

    request232.GET('/oib/static/common/js/3p/prototype.js')

    request233.GET('/oib/static/common/js/3p/jqueryui/ui.tabs.js')

    request234.GET('/oib/static/common/js/3p/autoresize.jquery.min.js')

    request235.GET('/oib/static/common/js/3p/jquery.tooltip.js')

    request236.GET('/oib/static/js/standardsBrowser/standards.js')

    grinder.sleep(11)
    request237.GET('/oib/static/common/js/widgets/BackspaceSuppress.js')

    request238.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/js/math-utilities.js')

    request239.GET('/oib/static/js/standardsBrowser/standardsUi.js')

    request240.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/js/LaTeXMathML.js')

    request241.GET('/oib/static/common/js/widgets/TimeoutDetect.js')

    request242.GET('/oib/static/js/wgen.oib.utilities.js')

    request243.GET('/oib/static/common/js/3p/RoboHelp_CSH.js')

    request244.GET('/oib/static/js/global_ready.js')

    request245.GET('/oib/static/js/jquery_functions.js')

    request246.GET('/oib/static/common/js/widgets/help.js')

    request247.GET('/oib/static/js/cookieHandler.js')

    request248.GET('/oib/static/js/ViewItemBankEntity.js')

    request249.GET('/oib/static/js/widgets/SharingDropdown.js')

    request250.GET('/oib/static/js/EntityPopupSourceUI.js')

    request251.GET('/oib/static/common/js/3p/jqueryMultiSelect.js')

    request252.GET('/oib/static/js/manage/ManageBrowserRenderer.js')

    request253.GET('/oib/static/common/js/3p/googleAnalytics.js')

    request254.GET('/oib/static/js/widgets/tooltip.js')

    request255.GET('/oib/static/js/manage/ManageItemBrowserRenderer.js')

    request256.GET('/oib/static/js/standardsBrowser/viewStandardsUi.js')

    request257.GET('/oib/static/js/manage/ManagePassageBrowserRenderer.js')

    request258.GET('/oib/static/js/widgets/sharing.js')

    request259.GET('/oib/static/js/standardsBrowser/createStandardsUi.js')

    request260.GET('/oib/static/js/manage/ManageBrowser.js')

    request261.GET('/oib/static/common/images/icon_question_contextual.gif')

    request262.GET('/oib/static/images/navigation/navbar_logo.gif')

    grinder.sleep(130)
    request263.GET('/oib/static/common/images/mclass/bg_header_blue_dot.gif')

    request264.GET('/oib/static/images/top_bar_divider.gif')

    request265.GET('/oib/static/images/navigation/navigation_buttons_sprite.png')

    request266.GET('/oib/static/images/navigation/navigation_buttons_icons_sprite.png')

    request267.GET('/oib/static/images/assessment/assess_back.png')

    request268.GET('/oib/static/images/dashboard/video_box_gradient.png')

    request269.GET('/oib/static/images/table_contents_right_tile.gif')

    request270.GET('/oib/static/images/sprites/table_contents_corners_sprite.gif')

    request271.GET('/oib/static/images/table_contents_bottom_tile.gif')

    request272.GET('/oib/static/images/ajax-loader-lrg.gif')

    request273.GET('/oib/static/images/sprites/body_content_area_corner_sprite.png')

    grinder.sleep(82)
    request274.GET('/oib/static/js/manage/ManageRubricBrowserRenderer.js')

    request275.GET('/oib/static/js/manage/ManageAssessmentBrowserRenderer.js')

    request276.GET('/oib/static/js/dashboard/widgets/RecentEntityWidget.js')

    request277.GET('/oib/static/js/dashboard/dashboard_ready.js')

    request278.GET('/oib/static/js/dashboard/DashboardPage.js')

    request279.GET('/oib/static/js/item/question/QuestionType.js')

    request280.GET('/oib/static/js/item/question/OpenResponseQuestionType.js')

    request281.GET('/oib/static/common/js/widgets/GlobalNavBar.js')

    return result

  def page3(self):
    """GET ga.js (request 301)."""
    result = request301.GET('/ga.js')

    return result

  def page4(self):
    """GET recent (requests 401-402)."""
    self.token_type = \
      'all'
    self.token_pageSize = \
      '50'
    self.token_page = \
      '0'
    self.token__ = \
      '1295886908585'
    result = request401.GET('/oib/webservices/entities/recent' +
      '?type=' +
      self.token_type +
      '&pageSize=' +
      self.token_pageSize +
      '&page=' +
      self.token_page +
      '&_=' +
      self.token__)

    request402.GET('/oib/static/images/buttons/blue_button_flat.gif')

    return result

  def page5(self):
    """GET ellipsis.xml (requests 501-504)."""
    result = request501.GET('/oib/static/common/css/ellipsis.xml')

    grinder.sleep(70)
    request502.GET('/oib/static/images/manage/locate_rounded_corner_objects.png')

    grinder.sleep(33)
    request503.GET('/oib/static/images/view_overlay/sprites.png')

    request504.GET('/oib/static/images/manage/assessment_item_count_box.png')

    return result

  def page6(self):
    """GET create (requests 601-603)."""
    self.token_fromManage = \
      'false'
    result = request601.GET('/oib/passage/create' +
      '?fromManage=' +
      self.token_fromManage)

    grinder.sleep(41)
    request602.GET('/oib/static/css/create/create.css')

    request603.GET('/oib/static/images/tooltips/tooltip_win_arrow_top.png')

    return result

  def page7(self):
    """GET empty.html (requests 701-757)."""
    result = request701.GET('/oib/static/empty.html')

    grinder.sleep(12)
    request702.GET('/oib/static/images/sprites/dropdown_top_bottom_sprite.png')

    request703.GET('/oib/static/images/sprites/dropdown_sides.png')

    request704.GET('/oib/static/images/connectors/create_box_bottom_connector.png')

    request705.GET('/oib/static/images/connectors/create_box_top_connector.png')

    request706.GET('/oib/static/images/sprites/slider_sprite.png')

    request707.GET('/oib/static/images/connectors/create_box_bottom.png')

    grinder.sleep(17)
    request708.GET('/oib/static/images/connectors/create_box_bkgrd.png')

    request709.GET('/oib/static/images/connectors/create_box_top.png')

    grinder.sleep(57)
    request710.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/tiny_mce.js')

    request711.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelveimage/js/threetwelveImage.js')

    grinder.sleep(13)
    request712.GET('/oib/static/js/widgets/SubjectDropdown.js')

    request713.GET('/oib/static/js/widgets/EditPageSubjectDropdown.js')

    request714.GET('/oib/static/common/js/widgets/tooltip.js')

    request715.GET('/oib/static/common/js/wgen/threetwelve/Ajax.js')

    request716.GET('/oib/static/js/EditPage.js')

    request717.GET('/oib/static/js/StyledTextEditor.js')

    request718.GET('/oib/static/js/widgets/sliders/TimeSlider.js')

    request719.GET('/oib/static/js/widgets/sliders/GradeRangeSlider.js')

    request720.GET('/oib/static/js/widgets/collapsible_panel.js')

    request721.GET('/oib/static/js/passage/Passage.js')

    request722.GET('/oib/static/js/widgets/dialog.js')

    request723.GET('/oib/static/js/EditReady.js')

    grinder.sleep(452)
    request724.GET('/oib/static/images/slider.png')

    grinder.sleep(24)
    request725.GET('/oib/static/images/create/btn_section_expander_item_closed.png')

    request726.GET('/oib/static/images/create/btn_section_expander_item.png')

    grinder.sleep(40028)
    request727.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/langs/en.js')

    request728.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/editor_template.js')

    request729.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelveimage/editor_plugin.js')

    request730.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/advimagescale/editor_plugin.js')

    request731.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/editor_plugin.js')

    request732.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/atomic/editor_plugin.js')

    grinder.sleep(14)
    request733.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/autoresize/editor_plugin.js')

    request734.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/editor_plugin.js')

    request735.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/table/editor_plugin.js')

    request736.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/paste/editor_plugin.js')

    request737.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/editor_plugin.js')

    request738.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/langs/en.js')

    request739.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/inlinepopups/editor_plugin.js')

    grinder.sleep(34)
    request740.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui.css')

    request741.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/ui_threetwelve.css')

    request742.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/inlinepopups/skins/clearlooks2/window.css')

    grinder.sleep(116)
    request743.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/img/button_bg.png')

    request744.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/img/icons.gif')

    request745.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/img/small.png')

    request746.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/img/medium.png')

    request747.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvefontsize/img/large.png')

    request748.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/latexmath/img/ed_mathformula.gif')

    request749.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_space_title_2.gif')

    request750.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_space_title_1.gif')

    request751.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_space_title_3.gif')

    request752.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_add_space_ruled.png')

    request753.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/plugins/threetwelvespace/img/btn_wysiwyg_add_space_unruled.png')

    grinder.sleep(51)
    request754.GET('/oib/static/tinymce-jquery/js/3p/jscripts/tiny_mce/themes/advanced/skins/o2k7/content.css')

    grinder.sleep(8460)
    request755.GET('/oib/static/images/view_overlay/border.png')

    request756.GET('/oib/static/images/view_overlay/close_X.png')

    request757.GET('/oib/static/images/sprites/buttons.png')

    return result

  def page8(self):
    """POST previewPassage (request 801)."""
    result = request801.POST('/oib/previewPassage',
      ( NVPair('contentJSON', '{\"passageType\": \"2\", \"body\": \"<p>Load test passage content</p>\", \"title\": \"Load test passage\", \"subjectCode\": \"ELA\", \"estTimeSecs\": 180, \"alignGrade\": {\"from\": \"6\", \"to\": \"8\"}}'), ),
      ( NVPair('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'), ))

    return result

  def page9(self):
    """GET keepalive (request 901)."""
    self.token__ = \
      '1295886990210'
    result = request901.GET('/oib/keepalive' +
      '?_=' +
      self.token__)

    return result

  def page10(self):
    """POST sharingAgreement (request 1001)."""
    result = request1001.POST('/oib/sharingAgreement',
      '',
      ( NVPair('Content-Type', 'text/plain; charset=UTF-8'), ))

    return result

  def page11(self, csrfToken):
    jsonArgs = {'passageType': '2',
                'body': "<p>Load test passage content</p>",
                'title': "Load test passage5",
                'subjectCode': "ELA",
                'estTimeSecs': '180',
                'alignGrade': {'from': '6', 'to': '8'}}
    result = self.savePassage(1101, url0, csrfToken, jsonArgs)
    return result

  def page12(self):
    """GET create (request 1201)."""
    self.token_id = \
      '1392'
    result = request1201.GET('/oib/passage/create' +
      '?fromManage=' +
      self.token_fromManage +
      '&id=' +
      self.token_id)

    return result

  def page13(self):
    """GET home (request 1301)."""
    result = request1301.GET('/oib/home')

    return result

  def page14(self):
    """GET recent (request 1401)."""
    self.token__ = \
      '1295887065890'
    result = request1401.GET('/oib/webservices/entities/recent' +
      '?type=' +
      self.token_type +
      '&pageSize=' +
      self.token_pageSize +
      '&page=' +
      self.token_page +
      '&_=' +
      self.token__)

    return result

  def page15(self):
    """GET logout (requests 1501-1502)."""
    
    # Expecting 302 'Moved Temporarily'
    result = request1501.GET('/oib/logout')

    request1502.GET('/wgen/Logout.do')

    return result

  def getCsrfToken(self, result):
    import re
    resultString = result.text
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

  def __call__(self):
    """This method is called for every run performed by the worker thread."""
    self.page1()      # GET login (requests 101-102)

    # grinder.sleep(9802)
    self.page2()      # POST login (requests 201-281)

    # grinder.sleep(207)
    self.page3()      # GET ga.js (request 301)

    # grinder.sleep(159)
    self.page4()      # GET recent (requests 401-402)

    # grinder.sleep(20)
    self.page5()      # GET ellipsis.xml (requests 501-504)

    # grinder.sleep(18945)
    createPage = self.page6()      # GET create (requests 601-603)
    csrfToken = self.getCsrfToken(createPage)

    # grinder.sleep(15)
    self.page7()      # GET empty.html (requests 701-757)

    # grinder.sleep(13)
    self.page8()      # POST previewPassage (request 801)

    # grinder.sleep(10978)
    self.page9()      # GET keepalive (request 901)

    # grinder.sleep(25264)
    self.page10()     # POST sharingAgreement (request 1001)

    # grinder.sleep(17693)
    savePassageResult = self.page11(csrfToken)
    passageVcid = json.loads(savePassageResult.text)['vcid']

    # grinder.sleep(15787)
    self.page12()     # GET create (request 1201)

    # grinder.sleep(15333)
    self.page13()     # GET home (request 1301)

    # grinder.sleep(405)
    self.page14()     # GET recent (request 1401)

    # grinder.sleep(9862)
    self.page15()     # GET logout (requests 1501-1502)


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
instrumentMethod(Test(1100, 'Page 11'), 'savePassage')
instrumentMethod(Test(1200, 'Page 12'), 'page12')
instrumentMethod(Test(1300, 'Page 13'), 'page13')
instrumentMethod(Test(1400, 'Page 14'), 'page14')
instrumentMethod(Test(1500, 'Page 15'), 'page15')
