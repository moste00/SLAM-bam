
"use strict";

let alarmmonitor = require('./alarmmonitor.js');
let Interfaces = require('./Interfaces.js');
let StringArray = require('./StringArray.js');
let Pose2DArray = require('./Pose2DArray.js');
let PantiltStatus = require('./PantiltStatus.js');
let ArmStatus = require('./ArmStatus.js');
let WatchdogStatus = require('./WatchdogStatus.js');
let MotorCurrent = require('./MotorCurrent.js');
let MotorsStatus = require('./MotorsStatus.js');
let LaserMode = require('./LaserMode.js');
let StringStamped = require('./StringStamped.js');
let SubState = require('./SubState.js');
let PantiltStatusStamped = require('./PantiltStatusStamped.js');
let inputs_outputs = require('./inputs_outputs.js');
let named_inputs_outputs = require('./named_inputs_outputs.js');
let BatteryStatus = require('./BatteryStatus.js');
let named_input_output = require('./named_input_output.js');
let ElevatorStatus = require('./ElevatorStatus.js');
let InverterStatus = require('./InverterStatus.js');
let OdomManualCalibrationStatusStamped = require('./OdomManualCalibrationStatusStamped.js');
let Data = require('./Data.js');
let LaserStatus = require('./LaserStatus.js');
let Axis = require('./Axis.js');
let BoolArray = require('./BoolArray.js');
let AlarmSensor = require('./AlarmSensor.js');
let Pose2DStamped = require('./Pose2DStamped.js');
let SafetyModuleStatus = require('./SafetyModuleStatus.js');
let RobotnikMotorsStatus = require('./RobotnikMotorsStatus.js');
let WatchdogStatusArray = require('./WatchdogStatusArray.js');
let Alarms = require('./Alarms.js');
let MotorStatus = require('./MotorStatus.js');
let OdomCalibrationStatusStamped = require('./OdomCalibrationStatusStamped.js');
let QueryAlarm = require('./QueryAlarm.js');
let encoders = require('./encoders.js');
let alarmsmonitor = require('./alarmsmonitor.js');
let BatteryDockingStatusStamped = require('./BatteryDockingStatusStamped.js');
let MotorsStatusDifferential = require('./MotorsStatusDifferential.js');
let Register = require('./Register.js');
let ElevatorAction = require('./ElevatorAction.js');
let MotorReferenceValue = require('./MotorReferenceValue.js');
let ReturnMessage = require('./ReturnMessage.js');
let Registers = require('./Registers.js');
let ptz = require('./ptz.js');
let OdomCalibrationStatus = require('./OdomCalibrationStatus.js');
let BatteryDockingStatus = require('./BatteryDockingStatus.js');
let PresenceSensorArray = require('./PresenceSensorArray.js');
let OdomManualCalibrationStatus = require('./OdomManualCalibrationStatus.js');
let PresenceSensor = require('./PresenceSensor.js');
let State = require('./State.js');
let BatteryStatusStamped = require('./BatteryStatusStamped.js');
let MotorPID = require('./MotorPID.js');
let MotorReferenceValueArray = require('./MotorReferenceValueArray.js');
let MotorHeadingOffset = require('./MotorHeadingOffset.js');
let Cartesian_Euler_pose = require('./Cartesian_Euler_pose.js');
let SetElevatorFeedback = require('./SetElevatorFeedback.js');
let SetElevatorResult = require('./SetElevatorResult.js');
let SetElevatorActionFeedback = require('./SetElevatorActionFeedback.js');
let SetElevatorAction = require('./SetElevatorAction.js');
let SetElevatorActionGoal = require('./SetElevatorActionGoal.js');
let SetElevatorActionResult = require('./SetElevatorActionResult.js');
let SetElevatorGoal = require('./SetElevatorGoal.js');

module.exports = {
  alarmmonitor: alarmmonitor,
  Interfaces: Interfaces,
  StringArray: StringArray,
  Pose2DArray: Pose2DArray,
  PantiltStatus: PantiltStatus,
  ArmStatus: ArmStatus,
  WatchdogStatus: WatchdogStatus,
  MotorCurrent: MotorCurrent,
  MotorsStatus: MotorsStatus,
  LaserMode: LaserMode,
  StringStamped: StringStamped,
  SubState: SubState,
  PantiltStatusStamped: PantiltStatusStamped,
  inputs_outputs: inputs_outputs,
  named_inputs_outputs: named_inputs_outputs,
  BatteryStatus: BatteryStatus,
  named_input_output: named_input_output,
  ElevatorStatus: ElevatorStatus,
  InverterStatus: InverterStatus,
  OdomManualCalibrationStatusStamped: OdomManualCalibrationStatusStamped,
  Data: Data,
  LaserStatus: LaserStatus,
  Axis: Axis,
  BoolArray: BoolArray,
  AlarmSensor: AlarmSensor,
  Pose2DStamped: Pose2DStamped,
  SafetyModuleStatus: SafetyModuleStatus,
  RobotnikMotorsStatus: RobotnikMotorsStatus,
  WatchdogStatusArray: WatchdogStatusArray,
  Alarms: Alarms,
  MotorStatus: MotorStatus,
  OdomCalibrationStatusStamped: OdomCalibrationStatusStamped,
  QueryAlarm: QueryAlarm,
  encoders: encoders,
  alarmsmonitor: alarmsmonitor,
  BatteryDockingStatusStamped: BatteryDockingStatusStamped,
  MotorsStatusDifferential: MotorsStatusDifferential,
  Register: Register,
  ElevatorAction: ElevatorAction,
  MotorReferenceValue: MotorReferenceValue,
  ReturnMessage: ReturnMessage,
  Registers: Registers,
  ptz: ptz,
  OdomCalibrationStatus: OdomCalibrationStatus,
  BatteryDockingStatus: BatteryDockingStatus,
  PresenceSensorArray: PresenceSensorArray,
  OdomManualCalibrationStatus: OdomManualCalibrationStatus,
  PresenceSensor: PresenceSensor,
  State: State,
  BatteryStatusStamped: BatteryStatusStamped,
  MotorPID: MotorPID,
  MotorReferenceValueArray: MotorReferenceValueArray,
  MotorHeadingOffset: MotorHeadingOffset,
  Cartesian_Euler_pose: Cartesian_Euler_pose,
  SetElevatorFeedback: SetElevatorFeedback,
  SetElevatorResult: SetElevatorResult,
  SetElevatorActionFeedback: SetElevatorActionFeedback,
  SetElevatorAction: SetElevatorAction,
  SetElevatorActionGoal: SetElevatorActionGoal,
  SetElevatorActionResult: SetElevatorActionResult,
  SetElevatorGoal: SetElevatorGoal,
};
