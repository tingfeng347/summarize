package com.atguigu.myzhxy.pojo;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

/**
 * @project: sms
 * @description: 班级信息
 */
@Data
@TableName("tb_clazz")
public class Clazz {
    //班级信息
    @TableId(value = "id",type = IdType.AUTO)
    private Integer id;             //班级Id
    private String name;            //负责人名称
    private String number;          //教室容纳人数
    private String introducation;   //教师电话
    //班主任信息
    private String headmaster;      //教师名称
    private String telephone;       //教师电话
    private String email;           //教师邮箱
    //教室名称
    private String gradeName;      //班级教室名称


}
