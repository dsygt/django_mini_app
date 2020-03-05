// pages/jokes/jokes.js
Page({
  /**
   * 页面的初始数据
   */
  data: {
    content:null 
  },
  /**
   * 生命周期函数--监听页面加载 这个也没改吧 ,都是下午你改的,我就没怎么改  你改过那里了
   */  
  onLoad: function (options) {
    var timestamp = Date.parse(new Date())/1000;
    var that = this
    console.log('时间戳:',timestamp),
    wx.request({
      url: 'http://v.juhe.cn/joke/content/list.php?sort=desc&page=&pagesize=&time=' + timestamp+'&key=ceb3ad871a9849bae1e7569d17f95855',
      success:function(res){
        console.log('成功了,,,', res.data.result.data)
        that.setData({content:res.data.result.data})

      },
      fail:function(res){
        console.log('失败了',res.errMsg)
      }
    })
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})