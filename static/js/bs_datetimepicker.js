$("#dateTime").datetimepicker({
      language: 'zh-CN',//语言
      format: 'yyyy-mm-dd hh:ii:ss', //String 默认值: 'mm/dd/yyyy'日期转换格式
      autoclose: true, //Boolean 默认值:false 选择完日期自动关闭
      //startView: 2,//Number, String. 默认值：2, 'month' 日期时间选择器打开之后首先显示的视图。
      //minView: 0,//Number, String. 默认值：0, 'hour' 日期时间选择器所能够提供的最精确的时间选择视图
      weekStart: 1,//默认值:0. 0(星期日)到6(星期六)
      startDate: new Date("1997/1/1"),//Date类型,默认值：开始时间.不能小于开始时间
      //endDate: //Date类型,默认值：结束时间.不能大于开始时间
      //daysOfWeekDisabled: [0,1,2,3,4,5,6] //String,Array类型.默认值:"",[]. 不能被选择的week
      todayBtn: "linked",//Boolean, "linked". 默认值: false 如果此值为true 或 "linked"，则在日期时间选择器组件的底部显示一个 "Today" 按钮用以选择当前日期。如果是true的话，"Today" 按钮仅仅将视图转到当天的日期，如果是"linked"，当天日期将会被选中。
      todayHighlight: true,//Boolean. 默认值: false 如果为true, 高亮当前日期。
      keyboardNavigation: true,//Boolean. 默认值: true 是否允许通过方向键改变日期。
      forceParse: true,//Boolean. 默认值: true  当选择器关闭的时候，是否强制解析输入框中的值。也就是说，当用户在输入框中输入了不正确的日期，选择器将会尽量解析输入的值，并将解析后的正确值按照给定的格式format设置到输入框中。
      minuteStep: 10,//Number. 默认值: 5
      //pickerPosition: //String. 默认值: 'bottom-right' (还支持 : 'bottom-left') 此选项当前只在组件实现中提供支持。通过设置选项可以讲选择器放倒输入框下方
      //viewSelect: 2,//不知道
      initialDate: "2015/5/5",//Date or String. 默认值: new Date() 初始化日期
      showMeridian: true//Boolean. 默认值: false 以12小时制显示
    });