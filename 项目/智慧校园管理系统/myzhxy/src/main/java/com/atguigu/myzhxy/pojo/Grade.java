package com.atguigu.myzhxy.pojo;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

/**
 * @project: sms
 * @description: 年级及预定人信息
 */
@Data
@TableName("tb_classroom")
public class Grade {

    //年级信息
    @TableId(value = "id",type = IdType.AUTO)
    private Integer id;             //年级ID
    private String name;            //教室名称
    private String introducation;   //预定科目及上课时间
    //预定人信息
    private String manager;         //预定人姓名
    private String email;           //预定人邮箱
    private String telephone;       //预定人电话

}