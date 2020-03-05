// pages/ceshi/ceshi.js
const app = getApp()
Page({
  data:{
    list:null
  },
  text_network:function(){
    var that = this
    wx.request({
      url: 'http://v.juhe.cn/dream/category?fid=%E6%9D%9C%E5%B0%91%E6%AF%85&key=cad5055003636967696a2c0d81fca82c',
      method:'GET',
      header:{},
      success:function(res){
        //将获取到的json数据，存在名字叫list的这个数组中
        that.setData({
          list: res.data.result,
        //res代表success函数的事件对，data是固定的，list是数组
        })
        console.log('结果success:'+res.data.result)
      },
      fail: function (res) {
        console.log('结果fail:' + res.errMsg)
      }
    })
  },
// 保存数据
  save_data:function(){
    console.log('save...')
    wx.setStorage({
      key: 'text',
      data: '我是被保存的数据',
    })
  },
  // 读取
  read_data:function(){
    wx.getStorage({
      key: 'text',
      success: function(res) {
        console.log('读取成功:'+res.data)
      },
      fail: function (res) { 
        console.log('读取失败。。。'+res.errMsg)
      },
    })
  },
// 清除当前缓存
  remove_data:function(){
    wx.removeStorage({
      key: 'text',
      success: function(res) {
        console.log('清除缓存成功')
      },
      fail:function(res){
        console.log('清除缓存失败。。。')
      }
    })
  },
// 清空所有
  clear_data:function(){
    console.log('清空成功')
    wx.clearStorage()
  },

  //事件处理函数
  bindViewTap:function(){},
  /**
   * 页面的初始数据
   */
  data: {
    array: app.globalData.abc
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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