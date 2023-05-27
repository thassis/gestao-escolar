import EventsAddPhotos from "pages/events-add-photos/EventsAddPhotos";
import EventsDescription from "pages/events-description/EventsDescription";
import EventsNext from "pages/events-next/EventsNext";
import EventsOld from "pages/events-old/EventsOld";
import EventsRegister from "pages/events-register/EventsRegister";
import Home from "pages/home/Home";
import Login from "pages/login/Login"
import NoPage from "pages/no-page/NoPage";
import RegisterStudent from "pages/register-student/RegisterStudent";
import ScheduledEvents from "pages/scheduled-events/ScheduledEvents";
import ListStudent from "pages/student-list/ListStudent";
import EditRegisterStudent from "pages/student-list/EditRegisterStudent";
import { Route, Routes } from "react-router-dom"
import AttendanceList from "pages/presential-list/AttendanceList";


export const AppRoutes = () => {
  
    return (
        <Routes>
            <Route path="/">
              <Route index element={<Login />} />
              <Route path="/home" element={<Home />} />
              <Route path="register-student" element={<RegisterStudent />} />
              <Route path="scheduled-events" element={<ScheduledEvents />} />
              <Route path="events-next" element={<EventsNext />} />
              <Route path="events-old" element={<EventsOld />} />
              <Route path="events-register" element={<EventsRegister />} />
              <Route path="events-description" element={<EventsDescription />} />
              <Route path="events-add-photos" element={<EventsAddPhotos />} />
              <Route path="student-list" element={<ListStudent />} />
              <Route path="student-list/edit/:id" element={<EditRegisterStudent />} />
              <Route path="attendance-list" element={<AttendanceList />} />
              <Route path="*" element={<NoPage />} />
            </Route>
          </Routes>
    );
}