# received help from Asher G and Aneikan

import pytest
from unittest.mock import MagicMock
from wpilib import Encoder, PIDController
from climbramp import ClimbRamp
from drivetrian import Drivetrain
from pytest import MonkeyPatch

@pytest.fixture
def drivetrain()-> Drivetrain:
    drive = Drivetrain()
    drive.leftEncoder= MagicMock()
    drive.rightEncoder= MagicMock()
    drive.left_motor = MagicMock()
    drive.right_motor= MagicMock()
    drive.drive= MagicMock()
    drive.gyro= MagicMock()
    return drive

@pytest.mark.parametrize(('gyro_number', 'output'), (2 , True), (5, False) ))
def test_reached_top(drivetrain: Drivetrain, monkeypatch: MonkeyPatch, gyro_number, output) -> None:
        ramp= ClimbRamp(drivetrain)

        def mock_gyro(self):
            return gyro_value

        monkeypatch.setattr(mock_gyro, Drivetrain, 'getGyroAngleY', mock_gyro)

        # Action
        top = ramp.reached_top()

        # Assert
        assert top == output


@pytest.mark.parametrize(('gyro_number', 'output'), (2 , True), (5, False) ))
 def test_did_tip_up(mock_drivetrain, monkeypatch: MonkeyPatch, gyro_value, on_ramp)-> None:
        halfway = ClimbRamp(drivetrain)

        def mock_gyro(self):
            return gyro_value

        monkeypatch.setattr(mock_gyro, Drivetrain, 'getGyroAngleY',mock_gyro)

        # Action
       top = halfway.did_tip_up()

        # Assert
        assert top == on_ramp



def test_reset(drivetrain: Drivetrain)->None:
    halfway = ClimbRamp(drivetrain)
    halfway.forward = 0.7
    halfway.ended_ramp= True
    halfway.started_ramp = True


    ClimbRamp.reset()

    assert halfway.ended_ramp == False
    assert halfway.started_ramp == False
    assert halfway.forward == 0.8


