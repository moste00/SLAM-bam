
"use strict";

let get_mode = require('./get_mode.js')
let GetBool = require('./GetBool.js')
let SetNamedDigitalOutput = require('./SetNamedDigitalOutput.js')
let set_CartesianEuler_pose = require('./set_CartesianEuler_pose.js')
let SetElevator = require('./SetElevator.js')
let ack_alarm = require('./ack_alarm.js')
let SetMotorMode = require('./SetMotorMode.js')
let home = require('./home.js')
let set_float_value = require('./set_float_value.js')
let get_alarms = require('./get_alarms.js')
let SetMotorStatus = require('./SetMotorStatus.js')
let InsertTask = require('./InsertTask.js')
let QueryAlarms = require('./QueryAlarms.js')
let set_named_digital_output = require('./set_named_digital_output.js')
let SetByte = require('./SetByte.js')
let GetPOI = require('./GetPOI.js')
let SetTransform = require('./SetTransform.js')
let set_mode = require('./set_mode.js')
let set_analog_output = require('./set_analog_output.js')
let set_ptz = require('./set_ptz.js')
let enable_disable = require('./enable_disable.js')
let axis_record = require('./axis_record.js')
let GetMotorsHeadingOffset = require('./GetMotorsHeadingOffset.js')
let set_digital_output = require('./set_digital_output.js')
let get_digital_input = require('./get_digital_input.js')
let set_modbus_register = require('./set_modbus_register.js')
let SetInt16 = require('./SetInt16.js')
let get_modbus_register = require('./get_modbus_register.js')
let GetPTZ = require('./GetPTZ.js')
let SetEncoderTurns = require('./SetEncoderTurns.js')
let set_height = require('./set_height.js')
let ResetFromSubState = require('./ResetFromSubState.js')
let set_odometry = require('./set_odometry.js')
let SetString = require('./SetString.js')
let SetCurrent = require('./SetCurrent.js')
let SetLaserMode = require('./SetLaserMode.js')
let SetMotorPID = require('./SetMotorPID.js')
let SetBuzzer = require('./SetBuzzer.js')

module.exports = {
  get_mode: get_mode,
  GetBool: GetBool,
  SetNamedDigitalOutput: SetNamedDigitalOutput,
  set_CartesianEuler_pose: set_CartesianEuler_pose,
  SetElevator: SetElevator,
  ack_alarm: ack_alarm,
  SetMotorMode: SetMotorMode,
  home: home,
  set_float_value: set_float_value,
  get_alarms: get_alarms,
  SetMotorStatus: SetMotorStatus,
  InsertTask: InsertTask,
  QueryAlarms: QueryAlarms,
  set_named_digital_output: set_named_digital_output,
  SetByte: SetByte,
  GetPOI: GetPOI,
  SetTransform: SetTransform,
  set_mode: set_mode,
  set_analog_output: set_analog_output,
  set_ptz: set_ptz,
  enable_disable: enable_disable,
  axis_record: axis_record,
  GetMotorsHeadingOffset: GetMotorsHeadingOffset,
  set_digital_output: set_digital_output,
  get_digital_input: get_digital_input,
  set_modbus_register: set_modbus_register,
  SetInt16: SetInt16,
  get_modbus_register: get_modbus_register,
  GetPTZ: GetPTZ,
  SetEncoderTurns: SetEncoderTurns,
  set_height: set_height,
  ResetFromSubState: ResetFromSubState,
  set_odometry: set_odometry,
  SetString: SetString,
  SetCurrent: SetCurrent,
  SetLaserMode: SetLaserMode,
  SetMotorPID: SetMotorPID,
  SetBuzzer: SetBuzzer,
};
